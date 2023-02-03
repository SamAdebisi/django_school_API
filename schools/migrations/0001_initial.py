# Generated by Django 4.1.5 on 2023-02-03 20:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="CustomUser",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=255, unique=True, verbose_name="email address"
                    ),
                ),
                (
                    "user_type",
                    models.CharField(
                        choices=[(1, "HOD"), (2, "Staff"), (3, "Student")],
                        default=1,
                        max_length=10,
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Attendance",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("attendance_date", models.DateTimeField(auto_now_add=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Blogs",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=255)),
                ("body", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Courses",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("course_name", models.CharField(max_length=255)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Staffs",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=255)),
                ("password", models.CharField(max_length=255)),
                ("address", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now_add=True)),
                (
                    "admin",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Subjects",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("subject_name", models.CharField(max_length=255)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now_add=True)),
                (
                    "course_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="schools.courses",
                    ),
                ),
                (
                    "staff_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="schools.staffs"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Students",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=255)),
                ("password", models.CharField(max_length=255)),
                ("gender", models.CharField(max_length=255)),
                ("profile_pic", models.FileField(max_length=255, upload_to="")),
                ("address", models.TextField()),
                ("session_start_year", models.DateTimeField()),
                ("session_end_year", models.DateTimeField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now_add=True)),
                (
                    "admin",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "course_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="schools.courses",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="NotificationStudent",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("message", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now_add=True)),
                (
                    "student_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="schools.students",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="NotificationStaff",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("message", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now_add=True)),
                (
                    "staff_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="schools.staffs"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="LeaveReportStudent",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("leave_date", models.CharField(max_length=255)),
                ("leave_message", models.TextField()),
                ("leave_status", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now_add=True)),
                (
                    "student_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="schools.students",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="LeaveReportStaff",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("leave_date", models.CharField(max_length=255)),
                ("leave_message", models.TextField()),
                ("leave_status", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now_add=True)),
                (
                    "staff_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="schools.staffs"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="FeedBackStudent",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("feedback", models.CharField(max_length=255)),
                ("feedback_reply", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now_add=True)),
                (
                    "student_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="schools.students",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="FeedBackStaff",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("feedback", models.CharField(max_length=255)),
                ("feedback_reply", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now_add=True)),
                (
                    "staff_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="schools.staffs"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Events",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=255)),
                ("body", models.TextField()),
                ("location", models.CharField(max_length=255)),
                ("event_date", models.DateField()),
                ("event_time", models.TimeField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now_add=True)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="event",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Comments",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("comment", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now_add=True)),
                ("author", models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                (
                    "blog",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="schools.blogs",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="AttendanceReport",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("status", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now_add=True)),
                (
                    "attendance_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="schools.attendance",
                    ),
                ),
                (
                    "student_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="schools.students",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="attendance",
            name="subject_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING, to="schools.subjects"
            ),
        ),
        migrations.CreateModel(
            name="AdminHOD",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=255)),
                ("password", models.CharField(max_length=255)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "admin",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
