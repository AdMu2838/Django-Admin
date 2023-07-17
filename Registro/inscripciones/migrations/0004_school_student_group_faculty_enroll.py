# Generated by Django 4.2.3 on 2023-07-17 20:09

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('inscripciones', '0003_user_teacher_assignment_user_unique_user_dni_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('school_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('school_name', models.CharField(max_length=100)),
                ('school_status', models.BooleanField(default=True)),
                ('school_created', models.DateTimeField(auto_now_add=True)),
                ('school_modified', models.DateTimeField(auto_now=True)),
                ('organization_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inscripciones.organization')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('student_status', models.BooleanField(default=True)),
                ('student_created', models.DateTimeField(auto_now_add=True)),
                ('student_modified', models.DateTimeField(auto_now=True)),
                ('organization_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inscripciones.organization')),
                ('school_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inscripciones.school')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inscripciones.user')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('group_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('group_name', models.CharField(max_length=100)),
                ('group_status', models.BooleanField(default=True)),
                ('group_created', models.DateTimeField(auto_now_add=True)),
                ('group_modified', models.DateTimeField(auto_now=True)),
                ('assignment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inscripciones.assignment')),
                ('organization_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inscripciones.organization')),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inscripciones.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('faculty_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('faculty_name', models.CharField(max_length=100)),
                ('faculty_status', models.BooleanField(default=True)),
                ('faculty_created', models.DateTimeField(auto_now_add=True)),
                ('faculty_modified', models.DateTimeField(auto_now=True)),
                ('organization_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inscripciones.organization')),
            ],
        ),
        migrations.CreateModel(
            name='Enroll',
            fields=[
                ('enroll_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('enroll_status', models.BooleanField(default=True)),
                ('enroll_created', models.DateTimeField(auto_now_add=True)),
                ('enroll_modified', models.DateTimeField(auto_now=True)),
                ('group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inscripciones.group')),
                ('organization_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inscripciones.organization')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inscripciones.student')),
            ],
        ),
    ]