from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Travel(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='travels',
        verbose_name="Пользователь"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название"
    )
    slug = models.SlugField(unique=True, verbose_name="Слаг")
    description = models.TextField(
        verbose_name="Описание"
    )
    location = models.CharField(
        max_length=255,
        verbose_name="Местоположение"
    )
    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True,
        verbose_name="Широта"
    )
    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True,
        verbose_name="Долгота"
    )
    cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Стоимость путешествия"
    )
    heritage_sites = models.CharField(
        max_length=255,
        verbose_name="Места культурного наследия"
    )
    recommended_places = models.CharField(
        max_length=255,
        verbose_name="Рекомендуемые места для посещения"
    )
    convenience_rating = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ],
        verbose_name="Оценка удобства передвижения"
    )
    safety_rating = models.IntegerField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ],
        verbose_name="Оценка безопасности"
    )
    population_density_rating = models.IntegerField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ],
        verbose_name="Оценка населенности"
    )
    vegetation_rating = models.IntegerField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ],
        verbose_name="Оценка растительности"
    )
    created_at = models.DateTimeField(
        default=timezone.now,
        verbose_name="Дата создания"
    )

    class Meta:
        verbose_name = "Путешествие"
        verbose_name_plural = "Путешествия"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Travel.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super(Travel, self).save(*args, **kwargs)


class TravelImage(models.Model):
    travel = models.ForeignKey(
        Travel,
        related_name='images',
        on_delete=models.CASCADE,
        verbose_name="Путешествие"
    )
    image = models.ImageField(
        upload_to='travel_images/',
        verbose_name="Изображение"
    )
    caption = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Подпись"
    )

    class Meta:
        verbose_name = "Фотография путешествия"
        verbose_name_plural = "Фотографии путешествий"

    def __str__(self):
        return f"Фото для {self.travel.title} - {self.caption}"
