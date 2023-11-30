# Generated by Django 4.2.7 on 2023-11-26 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        (
            "degree_checklist",
            "0007_rename_degreespecific_requirement_includesdegreespecific_degreespecific_requirement_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="includes",
            name="degree_program",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="degree_checklist.degreeprogram",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="includesdegreespecific",
            name="degree_program",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="degree_checklist.degreeprogram",
            ),
            preserve_default=False,
        ),
    ]