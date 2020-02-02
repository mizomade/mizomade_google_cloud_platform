from wagtail.admin.edit_handlers import (FieldPanel, FieldRowPanel,
                                         InlinePanel, MultiFieldPanel,
                                         PageChooserPanel, StreamFieldPanel)
from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock


class ColumnBlock(blocks.StreamBlock):
    heading = blocks.CharBlock(classname="full title")
    paragraph = blocks.RichTextBlock()
    image = ImageChooserBlock()

    class Meta:
        template = 'blog/blocks/column.html'


class TwoColumnBlock(blocks.StructBlock):

    left_column = ColumnBlock(icon='arrow-right', label='Left column content')
    right_column = ColumnBlock(icon='arrow-right', label='Right column content')

    class Meta:
        template = 'blog/blocks/two_column_block.html'
        icon = 'placeholder'
        label = 'Two Columns'





class HeadingBlock(blocks.StructBlock):
    text=blocks.CharBlock(required=True)
    size=blocks.ChoiceBlock(
        choices=[
        ('h2',"H2"),
        ('h3',"H3")
        ],required=True
    )

    class Meta:
        icon='title'
        label="Heading"
        template="blog/blocks/block_heading.html"


class VideoEmbedBlock(blocks.StructBlock):
    video = EmbedBlock(
       required=True,
       help_text="Insert a video url ",
       
   )

    class Meta:
        icon = 'media'
        label = "Embed Video"
        width = "30px"
        template = "blog/blocks/block_video_embed.html"

class BaseStream(blocks.StreamBlock):
    heads = HeadingBlock()
    video = VideoEmbedBlock()



class BaseImageInsertion(blocks.StructBlock):
    image = ImageChooserBlock()
    caption = blocks.CharBlock(required=False)
    class Meta:
        icon='image'
        label="images"
        template="blog/blocks/image_insertion.html"


class ImageInsertion(blocks.StreamBlock):
    heads = BaseImageInsertion()


class Quoting(blocks.StructBlock):
    quote = blocks.TextBlock(required=True, help_text="Add your text")
    quotedby = blocks.CharBlock(required=False, help_text="Quoted by")

    class Meta:  # noqa
        template = "blog/blocks/quoting.html"
        icon = "quote"
        label = "quoting"


