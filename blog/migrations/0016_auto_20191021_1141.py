# Generated by Django 2.2.5 on 2019-10-21 11:41

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20191021_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='body',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(classname='full')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('embedded_video', wagtail.embeds.blocks.EmbedBlock(icon='media')), ('BaseStream', wagtail.core.blocks.StreamBlock([('heads', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(required=True)), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('h2', 'H2'), ('h3', 'H3')]))]))])), ('quote', wagtail.core.blocks.BlockQuoteBlock()), ('pages', wagtail.core.blocks.PageChooserBlock()), ('HTML', wagtail.core.blocks.RawHTMLBlock())]),
        ),
    ]