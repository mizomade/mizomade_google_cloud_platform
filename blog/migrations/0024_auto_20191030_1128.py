# Generated by Django 2.2.5 on 2019-10-30 11:28

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_auto_20191030_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='body',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(classname='full')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('embedded_video', wagtail.embeds.blocks.EmbedBlock(icon='media')), ('BaseStream', wagtail.core.blocks.StreamBlock([('heads', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(required=True)), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('h2', 'H2'), ('h3', 'H3')]))]))])), ('images', wagtail.core.blocks.StreamBlock([('heads', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('caption', wagtail.core.blocks.CharBlock(required=False))]))])), ('quoting', wagtail.core.blocks.StructBlock([('quote', wagtail.core.blocks.TextBlock(help_text='Add your text', required=True)), ('quotedby', wagtail.core.blocks.CharBlock(help_text='Quoted by', required=False))])), ('pages', wagtail.core.blocks.PageChooserBlock()), ('HTML', wagtail.core.blocks.RawHTMLBlock())]),
        ),
    ]
