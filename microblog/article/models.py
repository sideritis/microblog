from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from tag.models import Tag
from core.utils import image_directory_path

from .utils import validate_title


class PublishedManager(models.Manager):
    use_for_related_fields = True

    def published(self, **kwargs):
        return self.filter(publish=True, **kwargs)


class Article(models.Model):
    title = models.CharField(max_length=80, verbose_name=_('Title'), unique=True, validators=[validate_title])
    slug = models.SlugField(max_length=80, verbose_name=_('Slug'), unique=True)
    text = models.TextField(verbose_name=_('Text'))
    desc = models.CharField(verbose_name=_('Description'), default='', max_length=180)
    author = models.ForeignKey(User, verbose_name=_('Author'))
    creation_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=True, verbose_name=_('Image'), upload_to=image_directory_path)
    publish = models.BooleanField(default=False, verbose_name=_('Publish'))
    publish_date = models.DateTimeField(blank=True, null=True)
    tags = models.ManyToManyField(Tag, verbose_name=_('Tags'))

    objects = PublishedManager()

    class Meta:
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')

    def __str__(self):
        return self.title

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return None
