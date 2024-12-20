# Generated by Django 4.2.7 on 2023-11-26 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("degree_checklist", "0013_alter_includes_course"),
    ]

    operations = [
        migrations.AlterField(
            model_name="includesdegreespecific",
            name="course",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="includesdegreespecific_set",
                to="degree_checklist.course",
            ),
        ),
    ]
