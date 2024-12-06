from django.db import models

from wagtail.models import Orderable, Page
from wagtail.fields import RichTextField, StreamField
from wagtail.blocks import StructBlock, StreamBlock, CharBlock, RichTextBlock
from wagtail.admin.panels import FieldPanel
from wagtail.search import index
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.images.blocks import ImageChooserBlock

from modelcluster.fields import ParentalKey

from common_funcs.common import is_number, is_integer, calculate_regression, remove_html_tags

class BlogPostPage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = StreamField([
        ('heading', CharBlock(classname="full title")),
        ('paragraph', RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('document', DocumentChooserBlock()),
    ])

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('intro'),
        FieldPanel('body'),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        context['blog_posts'] = self.get_children().live().public().order_by('-first_published_at')
        return context

# Create your models here.
