# Generated by Django 4.2.7 on 2023-11-16 03:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AccountingRequirement",
            fields=[
                (
                    "AccountingReqID",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ("AccountingReqName", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="CoreRequirement",
            fields=[
                ("RequirementID", models.AutoField(primary_key=True, serialize=False)),
                ("RequirementName", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Course",
            fields=[
                ("CourseID", models.AutoField(primary_key=True, serialize=False)),
                ("CourseName", models.CharField(max_length=255)),
                ("Credits", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="DegreeProgram",
            fields=[
                ("ProgramID", models.AutoField(primary_key=True, serialize=False)),
                ("ProgramName", models.CharField(max_length=255)),
                ("TotalCredits", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Department",
            fields=[
                ("DepartmentID", models.AutoField(primary_key=True, serialize=False)),
                ("DepartmentName", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Student",
            fields=[
                ("StudentID", models.AutoField(primary_key=True, serialize=False)),
                ("FirstName", models.CharField(max_length=255)),
                ("LastName", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Requires",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "core_requirement",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="degree_checklist.corerequirement",
                    ),
                ),
                (
                    "degree_program",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="degree_checklist.degreeprogram",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="IncludesAccounting",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "accounting_requirement",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="degree_checklist.accountingrequirement",
                    ),
                ),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="degree_checklist.course",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Includes",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "core_requirement",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="degree_checklist.corerequirement",
                    ),
                ),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="degree_checklist.course",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Has",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "accounting_requirement",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="degree_checklist.accountingrequirement",
                    ),
                ),
                (
                    "degree_program",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="degree_checklist.degreeprogram",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="EnrollsIn",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "degree_program",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="degree_checklist.degreeprogram",
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="degree_checklist.student",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="degreeprogram",
            name="Department",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="degree_checklist.department",
            ),
        ),
        migrations.AddField(
            model_name="course",
            name="Department",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="degree_checklist.department",
            ),
        ),
        migrations.CreateModel(
            name="BelongsTo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "degree_program",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="degree_checklist.degreeprogram",
                    ),
                ),
                (
                    "department",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="degree_checklist.department",
                    ),
                ),
            ],
        ),
    ]
