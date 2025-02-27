# Generated by Django 3.1.14 on 2022-09-21 17:26

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contentshub', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='master',
            name='name',
        ),
        migrations.AddField(
            model_name='klass',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='생성일'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='klass',
            name='summary',
            field=models.CharField(default=1, max_length=100, verbose_name='요약'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='klass',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='수정일'),
        ),
        migrations.AddField(
            model_name='master',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='등록일'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='master',
            name='email',
            field=models.EmailField(default=1, max_length=100, unique=True, verbose_name='이메일'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='master',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='수정일'),
        ),
        migrations.AddField(
            model_name='master',
            name='username',
            field=models.CharField(default=1, max_length=20, verbose_name='이름'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='klass',
            name='master',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='master_klass', to='contentshub.master', verbose_name='강사'),
        ),
        migrations.AlterField(
            model_name='klass',
            name='title',
            field=models.CharField(max_length=50, verbose_name='제목'),
        ),
    ]
