import os
from tkinter import Image
from django.db import models
from django.conf import settings
from django.utils.text import slugify
from produto.templatetags import filters

# Create your models here.

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao_curta = models.TextField(
        max_length=255, blank=True, verbose_name="Descriçao")
    descricao_longa = models.TextField()
    imagem = models.ImageField(
        upload_to='produto_imagens/%Y/%m/%d', blank=True, null=True)
    slug = models.SlugField(unique=True,  blank=True, null=True)
    preco_marketing = models.FloatField(verbose_name="preço market")
    preco_marketing_promocional = models.FloatField(
        default=0, verbose_name="preço promocional")
    tipo = models.CharField(
        default='V',
        max_length=1,
        choices=(
            ('V', 'Variável'),
            ('S', 'Simples'),
        )
    )

    def get_preco_formatado(self):
        """Modificar formato de visualização"""
        return filters(self.preco_marketing)
    get_preco_formatado.short_description = "Preço"

    def get_preco_promocional_formatado(self):
        """Modificar formato de visualização"""
        return filters(self.preco_marketing_promocional)
    get_preco_promocional_formatado.short_description = "Preço promocional"

    @staticmethod
    def resize_image(img, new_width=800):
        img_full_path = os.path.join(settings.MEDIA_ROOT, img.name)
        img_pil = Image.open(img_full_path)
        original_width, original_height = img_pil.size

        if original_width <= new_width:
            img_pil.close()
            return

        new_height = round((new_height - original_height) / original_width)

        new_img = img_pil.resize((new_width, new_height), Image.LANCZOS)
        new_img.save(
            img_full_path,
            optimize=True,
            quality=50
        )

        print(original_height, original_width)

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = f"{slugify(self.nome)}"
            self.slug = slug

        """Redimensionar tamanho da  imagem para tamanho padrão"""
        super().save(*args, **kwargs)

        max_image_size = 800

        if self.imagem:
            self.resize_image(self.imagem, max_image_size)

    def __str__(self):
        return self.nome


class Variacao(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50, blank=True, null=True)
    preco = models.FloatField()
    preco_promocional = models.FloatField(default=0)
    estoque = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.nome or self.produto.nome

    class Meta:
        verbose_name = 'Variação'
        verbose_name_plural = 'Variações'
