from django import forms
from django.db import models

from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index
from wagtail.wagtailsnippets.models import register_snippet

class VrblogIndexPage(Page):
    intro = models.CharField(max_length=250)
    equirectangular_image = models.ForeignKey(
        'wagtailimages.Image', 
        null=True,
        blank=True,
        on_delete = models.SET_NULL, 
        related_name = '+',
        )

    def get_context(self, request):
        #Update context to include only published posts, in reverse order
        context = super(VrblogIndexPage, self).get_context(request)
        blogpages = self.get_children().live().order_by('-first_published_at')
        context['blogpages'] = blogpages
        return context

    def link_sizes(self):
        link_items = self.get_children().live().count()
        if link_items:
            link_sizes = {'module': 4/link_items, 
                'half': 4/link_items*0.5,
                'radius': 4/link_items*.25,
                'center': 4/link_items*0.75,}
            return link_sizes
        else:
            return None

    def link_position(self):
        live_children = self.get_children().live()
        if live_children:
            module = 4/live_children.count()
            link_position = {}
            x = 0
            blogpages = live_children.order_by('-first_published_at')
            for item in blogpages:
                link_position[module*x]=item
                x += 1
            return link_position
        else:
            return None

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full"),
        ImageChooserPanel('equirectangular_image'),
    ]

class VrblogPageTag(TaggedItemBase):
    content_object = ParentalKey('VrblogPage', related_name='tagged_items')

class VrblogPage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    equirectangular_image = models.ForeignKey(
        'wagtailimages.Image', 
        null=True,
        blank=True,
        on_delete = models.SET_NULL, 
        related_name = '+',
        )
    tags = ClusterTaggableManager(through=VrblogPageTag, blank=True)
    categories = ParentalManyToManyField('vrblog.VrblogCategory', blank=True)

    def gallery_sizes(self):
        gallery_items = self.gallery_images.count()
        if gallery_items:
            gallery_sizes = {'module': 4/gallery_items, 
                'half': 4/gallery_items/2,
                'height': 4/gallery_items/2*0.75,
                'center': 4/gallery_items*0.75,}
            return gallery_sizes
        else:
            return None

    def color(self):
        color=['red', 'blue', 'green', 'yellow', 'cyan', 'magenta',]
        return color

    def category_string(self):
        categories=self.categories.all()
        if categories:
            category_list=[]
            for category in categories:
                category_list.append(category.name)
            category_string = ", ".join(category_list)
            return category_string
        else:
            category_string = 'Uncategorized'
            return category_string

    def tag_string(self):
        tags=self.tags.all()
        if tags:
            tag_list=[]
            for tag in tags:
                tag_list.append(tag.name)
            tag_string = ", ".join(tag_list)
            return tag_string
        else:
            tag_string = 'None'
            return tag_string

    def gallery_position(self):
        gallery_count = self.gallery_images.count()
        if gallery_count:
            module = 4/gallery_count
            gallery_position = {}
            x = 0
            gallery_items = self.gallery_images.all()
            for item in gallery_items:
                gallery_position[module*x]=item
                x += 1
            return gallery_position
        else:
            return None

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        #index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('date'),
            FieldPanel('tags'),
            FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
        ], heading="VRblog Information"),
        FieldPanel('intro'),
        ImageChooserPanel('equirectangular_image'),
        InlinePanel('gallery_images', label="Text + Image Gallery",),
    ]

class VrblogPageGalleryImage(Orderable):
    page = ParentalKey(VrblogPage, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.TextField("Text",)

    panels = [
        FieldPanel('caption'),
        ImageChooserPanel('image'),
    ]

class VrblogIndexPageGalleryImage(Orderable):
    page = ParentalKey(VrblogIndexPage, related_name='index_gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.TextField("Text",)

    panels = [
        #FieldPanel('caption'),
        ImageChooserPanel('image'),
    ]

class VrblogTagIndexPage(Page):

    def get_context(self, request):
        #Filter by tags
        tag = request.GET.get('tag')
        blogpages = VrblogPage.objects.filter(tags__name=tag)
        #Update template context
        context = super(VrblogTagIndexPage, self).get_context(request)
        context['blogpages'] = blogpages
        return context

@register_snippet
class VrblogCategory(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )

    panels = [
        FieldPanel('name'),
        ImageChooserPanel('icon'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'vrblog categories'
