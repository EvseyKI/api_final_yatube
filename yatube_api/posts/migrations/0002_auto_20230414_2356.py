# Generated by Django 3.2.16 on 2023-04-14 23:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Может состоять из символов и цифр', max_length=200, verbose_name='Название группы')),
                ('slug', models.SlugField(help_text='Может состоять из кирилицы и цифр', unique=True, verbose_name='Идентификатор группы')),
                ('description', models.TextField(help_text='Краткое описание группы', verbose_name='Описание группы')),
            ],
            options={
                'verbose_name': ('Группа',),
                'verbose_name_plural': 'Группы',
            },
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': ('Комментарий',), 'verbose_name_plural': 'Комментарии'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': ('Запись',), 'verbose_name_plural': 'Записи'},
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(help_text='Это пользователь, написавший комментарий', on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='Имя автора коментария'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created',
            field=models.DateTimeField(auto_now_add=True, db_index=True, help_text='Присваивается автоматически', verbose_name='Дата публикации комментария'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(help_text='Пост, к которому относится комментарий', on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='posts.post', verbose_name='Название поста'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(help_text='Пишем в рамках приличия', verbose_name='Пишем, что душе угодно'),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(help_text='Пользователь, написавший текст', on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL, verbose_name='Автор текста'),
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default=1, help_text='Расположена над текстом', upload_to='posts/', verbose_name='Картинка'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, help_text='Это время создания даты, создается автоматически', verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(help_text='Пишите, что хотите в рамках приличия', verbose_name='Текст поста'),
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('following', models.ForeignKey(help_text='Пользователь, на которого подписались', on_delete=django.db.models.deletion.CASCADE, related_name='following', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('user', models.ForeignKey(help_text='Пользователь, который подписался', on_delete=django.db.models.deletion.CASCADE, related_name='follower', to=settings.AUTH_USER_MODEL, verbose_name='Подписчик')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='group',
            field=models.ForeignKey(blank=True, help_text='Указывать необязательно', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to='posts.group', verbose_name='Название группы'),
        ),
    ]