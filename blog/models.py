from django import forms
from django.db import models

# New imports added for ParentalKey, Orderable, InlinePanel, ImageChooserPanel

from modelcluster.fields import ParentalKey,ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

from taggit.managers import TaggableManager

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField,StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel ,MultiFieldPanel,StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock 

from .blocks import ColumnBlock,TwoColumnBlock,BaseStream,ImageInsertion,Quoting

from wagtail.snippets.models import register_snippet

from wagtail.core.blocks import BlockQuoteBlock,PageChooserBlock
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your models here.


@register_snippet
class BlogCategory(models.Model):
    name = models.CharField(max_length=200)
    icon = models.ForeignKey('wagtailimages.Image', related_name='+', on_delete=models.SET_NULL,
    null = True)
    categorycolor=models.CharField(max_length=50,
    null = True)

    panels = [
        FieldPanel('name'),
        ImageChooserPanel('icon'),
        FieldPanel('categorycolor'),
    ]

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'blog categories'
    
    

class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    def get_context(self,request):
        context = super().get_context(request)
        blogpages = self.get_children().live().order_by('-first_published_at')
        # blogpages = self.get_children().live()

        paginator = Paginator(blogpages, 10)
        blogpages = paginator.page(1)

        blogcatlist = BlogPage.objects.all().order_by('-first_published_at')
        paging = Paginator(blogcatlist,6)
        blogcatlist = paging.page(1)
        context['blogcatlist'] = blogcatlist
        context['cata'] = BlogCategory.objects.all().distinct()

        context['blogpages'] = blogpages
        return context

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]


class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'BlogPage',
        related_name='tagged_items',
        on_delete = models.CASCADE
    )



class BlogPage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    Author = models.CharField(max_length=250,null=True)
    body = StreamField([
        ('heading',blocks.CharBlock(classname="full")),
        ('paragraph',blocks.RichTextBlock()),
        ('image',ImageChooserBlock()),
        # ('embedded_video',EmbedBlock(icon='media')),
        ('BaseStream',BaseStream()),
        ('images',ImageInsertion()),
        ('quoting',Quoting()),
        ('pages',PageChooserBlock()),
        ('HTML',blocks.
        RawHTMLBlock()),

        
    ])

    tags = ClusterTaggableManager(through=BlogPageTag,blank=True)
    categories = ParentalManyToManyField('blog.BlogCategory',blank = True)
    # tak = TaggableManager()
    # related = tags.similar_objects()

    
    


    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
        index.FilterField('date'),
        

        index.SearchField('categories'),
        # index.SearchField('tags'),

    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('date'),
            FieldPanel('tags'),
            FieldPanel('categories',widget=forms.CheckboxSelectMultiple), 
        ], heading="Blog information"),
        FieldPanel('Author'),
        FieldPanel('intro'),
        # FieldPanel('body', classname="full"),
        StreamFieldPanel('body'),
        InlinePanel('gallery_images', label="Gallery images"),
    ]

    def get_context(self, request):

        # Filter by tag
        tag = request.GET.get('tag')
        blogpages = BlogPage.objects.filter(tags__name=tag)

        # Update template context
        context = super().get_context(request)
        context['blogpages'] = blogpages
        return context
    
    # def trag(self,request):
    #     tag = self.tags
    #     self.related = tag.tags.similar_objects()
    #     # context['blogpages'] = related
    #     return related
    # def trip_single(self,request, slug):
    #     self.trip = get_object_or_404(BlogPage, slug=slug)
    #     self.trip_related = trip.tags.similar_objects()
    #     return render(request, 'blog/trip_single.html', {'trip': trip, 'trip_related': trip_related})
    
class BlogTagIndexPage(Page):

    def get_context(self, request):

        # Filter by tag
        tag = request.GET.get('tag')
        blogpages = BlogPage.objects.filter(tags__name=tag)

        # Update template context
        context = super().get_context(request)
        context['blogpages'] = blogpages
        return context

class BlogPageGalleryImage(Orderable):
    page = ParentalKey(BlogPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]


class BlogCategoryIndexPage(Page):

    def get_context(self, request):

        # Filter by tag
        category = request.GET.get('category')
        blogpages = BlogPage.objects.filter(categories__name=category)

        # Update template context
        context = super().get_context(request)
        context['blogpages'] = blogpages
        return context

    