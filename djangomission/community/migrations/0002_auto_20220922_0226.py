# Generated by Django 3.1.14 on 2022-09-21 17:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contentshub', '0002_auto_20220922_0226'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='생성일'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='answer',
            name='master',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='master_answer', to='contentshub.master', verbose_name='강사'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='question_answer', to='community.question', verbose_name='질문'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='answer',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='수정일'),
        ),
        migrations.AddField(
            model_name='question',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='생성일'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='삭제여부'),
        ),
        migrations.AddField(
            model_name='question',
            name='klass',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='klass_question', to='contentshub.klass', verbose_name='강의'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='수정일'),
        ),
        migrations.AddField(
            model_name='question',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_question', to='accounts.user', verbose_name='수강생'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='answer',
            name='contents',
            field=models.TextField(max_length=500, verbose_name='내용'),
        ),
        migrations.AlterField(
            model_name='question',
            name='contents',
            field=models.TextField(max_length=200, verbose_name='내용'),
        ),
    ]
