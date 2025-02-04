from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Function",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("docstring", models.TextField(default="", blank=True)),
                ("code", models.TextField()),
                ("kwargs", models.CharField(max_length=200)),
                ("line_number", models.IntegerField()),
            ],
            options={
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="Inheritance",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                ("order", models.IntegerField()),
            ],
            options={
                "ordering": ("order",),
            },
        ),
        migrations.CreateModel(
            name="Klass",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("docstring", models.TextField(default="", blank=True)),
                ("line_number", models.IntegerField()),
                ("import_path", models.CharField(max_length=255)),
                ("docs_url", models.URLField(default="", max_length=255)),
            ],
            options={
                "ordering": ("module__name", "name"),
            },
        ),
        migrations.CreateModel(
            name="KlassAttribute",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("value", models.CharField(max_length=200)),
                ("line_number", models.IntegerField()),
                (
                    "klass",
                    models.ForeignKey(
                        on_delete=models.CASCADE,
                        related_name="attribute_set",
                        to="cbv.Klass",
                    ),
                ),
            ],
            options={
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="Method",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("docstring", models.TextField(default="", blank=True)),
                ("code", models.TextField()),
                ("kwargs", models.CharField(max_length=200)),
                ("line_number", models.IntegerField()),
                ("klass", models.ForeignKey(on_delete=models.CASCADE, to="cbv.Klass")),
            ],
            options={
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="Module",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("docstring", models.TextField(default="", blank=True)),
                ("filename", models.CharField(default="", max_length=511)),
            ],
        ),
        migrations.CreateModel(
            name="ModuleAttribute",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("value", models.CharField(max_length=200)),
                ("line_number", models.IntegerField()),
                (
                    "module",
                    models.ForeignKey(
                        on_delete=models.CASCADE,
                        related_name="attribute_set",
                        to="cbv.Module",
                    ),
                ),
            ],
            options={
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="Project",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                ("name", models.CharField(unique=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="ProjectVersion",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                ("version_number", models.CharField(max_length=200)),
                (
                    "project",
                    models.ForeignKey(on_delete=models.CASCADE, to="cbv.Project"),
                ),
            ],
            options={
                "ordering": ("-version_number",),
            },
        ),
        migrations.AddField(
            model_name="module",
            name="project_version",
            field=models.ForeignKey(on_delete=models.CASCADE, to="cbv.ProjectVersion"),
        ),
        migrations.AddField(
            model_name="klass",
            name="module",
            field=models.ForeignKey(on_delete=models.CASCADE, to="cbv.Module"),
        ),
        migrations.AddField(
            model_name="inheritance",
            name="child",
            field=models.ForeignKey(
                on_delete=models.CASCADE,
                related_name="ancestor_relationships",
                to="cbv.Klass",
            ),
        ),
        migrations.AddField(
            model_name="inheritance",
            name="parent",
            field=models.ForeignKey(on_delete=models.CASCADE, to="cbv.Klass"),
        ),
        migrations.AddField(
            model_name="function",
            name="module",
            field=models.ForeignKey(on_delete=models.CASCADE, to="cbv.Module"),
        ),
        migrations.AlterUniqueTogether(
            name="projectversion",
            unique_together={("project", "version_number")},
        ),
        migrations.AlterUniqueTogether(
            name="moduleattribute",
            unique_together={("module", "name")},
        ),
        migrations.AlterUniqueTogether(
            name="module",
            unique_together={("project_version", "name")},
        ),
        migrations.AlterUniqueTogether(
            name="klassattribute",
            unique_together={("klass", "name")},
        ),
        migrations.AlterUniqueTogether(
            name="klass",
            unique_together={("module", "name")},
        ),
        migrations.AlterUniqueTogether(
            name="inheritance",
            unique_together={("child", "order")},
        ),
    ]
