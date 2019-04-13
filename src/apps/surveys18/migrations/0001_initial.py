# Generated by Django 2.2 on 2019-04-13 08:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AgeScope',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True, verbose_name='Name')),
                ('group', models.IntegerField(verbose_name='Group')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated')),
            ],
            options={
                'verbose_name': 'AgeScope',
                'verbose_name_plural': 'AgeScope',
            },
        ),
        migrations.CreateModel(
            name='BuilderFileType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Name')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated')),
            ],
            options={
                'verbose_name': 'BuilderFileType',
                'verbose_name_plural': 'BuilderFileType',
            },
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(verbose_name='Code')),
                ('name', models.CharField(blank=True, max_length=10, null=True, verbose_name='Name')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated')),
            ],
            options={
                'verbose_name': 'LivestockUnit',
                'verbose_name_plural': 'LivestockUnit',
            },
        ),
        migrations.CreateModel(
            name='EducationLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(verbose_name='Code')),
                ('name', models.CharField(blank=True, max_length=20, null=True, verbose_name='Name')),
                ('age', models.IntegerField(blank=True, null=True, verbose_name='Age')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated')),
            ],
            options={
                'verbose_name': 'EducationLevel',
                'verbose_name_plural': 'EducationLevel',
            },
        ),
        migrations.CreateModel(
            name='FarmerWorkDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(verbose_name='Code')),
                ('name', models.CharField(blank=True, max_length=20, null=True, verbose_name='Name')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated')),
            ],
            options={
                'verbose_name': 'FarmerWorkDay',
                'verbose_name_plural': 'FarmerWorkDay',
            },
        ),
        migrations.CreateModel(
            name='FarmRelatedBusiness',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(verbose_name='Code')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Name')),
                ('has_extra', models.BooleanField(default=False, verbose_name='Has Extra')),
                ('has_business', models.BooleanField(default=True, verbose_name='Has Business')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated')),
            ],
            options={
                'verbose_name': 'FarmRelatedBusiness',
                'verbose_name_plural': 'FarmRelatedBusiness',
            },
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(verbose_name='Code')),
                ('name', models.CharField(blank=True, max_length=10, null=True, verbose_name='Name')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated')),
            ],
            options={
                'verbose_name': 'Gender',
                'verbose_name_plural': 'Gender',
            },
        ),
        migrations.CreateModel(
            name='IncomeRange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Name')),
                ('minimum', models.IntegerField(verbose_name='Minimum Income')),
                ('maximum', models.IntegerField(verbose_name='Maximum Income')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated')),
            ],
            options={
                'verbose_name': 'IncomeRange',
                'verbose_name_plural': 'IncomeRanges',
            },
        ),
        migrations.CreateModel(
            name='Lack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Name')),
                ('is_lack', models.BooleanField(default=False, verbose_name='Is Lack')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated')),
            ],
            options={
                'verbose_name': 'Lack',
                'verbose_name_plural': 'Lack',
            },
        ),
        migrations.CreateModel(
            name='LandStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True, verbose_name='Name')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated')),
            ],
            options={
                'verbose_name': 'LandStatus',
                'verbose_name_plural': 'LandStatus',
            },
        ),
        migrations.CreateModel(
            name='LifeStyle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(verbose_name='Code')),
                ('name', models.CharField(blank=True, max_length=20, null=True, verbose_name='Name')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated')),
            ],
            options={
                'verbose_name': 'LifeStyle',
                'verbose_name_plural': 'LifeStyle',
            },
        ),
        migrations.CreateModel(
            name='ManagementType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(verbose_name='Code')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Name')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated')),
            ],
            options={
                'verbose_name': 'ManagementType',
                'verbose_name_plural': 'ManagementType',
            },
        ),
        migrations.CreateModel(
            name='MarketType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Name')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated')),
            ],
            options={
                'verbose_name': 'MarketType',
                'verbose_name_plural': 'MarketTypes',
            },
        ),
        migrations.CreateModel(
            name='Month',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Name')),
                ('value', models.IntegerField(choices=[(1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')])),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated')),
            ],
            options={
                'verbose_name': 'Month',
                'verbose_name_plural': 'Month',
            },
        ),
        migrations.CreateModel(
            name='OtherFarmWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True, verbose_name='Name')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated')),
            ],
            options={
                'verbose_name': 'OtherFarmWork',
                'verbose_name_plural': 'OtherFarmWork',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Name')),
                ('code', models.CharField(max_length=50, verbose_name='Code')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Product',
            },
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Name')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated')),
            ],
        ),
        migrations.CreateModel(
            name='RefuseReason',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True, verbose_name='Name')),
                ('has_extra', models.BooleanField(default=False, verbose_name='Has Extra')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated')),
            ],
            options={
                'verbose_name': 'RefuseReason',
                'verbose_name_plural': 'RefuseReason',
            },
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(verbose_name='Code')),
                ('name', models.CharField(blank=True, max_length=20, null=True, verbose_name='Name')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated')),
            ],
            options={
                'verbose_name': 'Relationship',
                'verbose_name_plural': 'Relationship',
            },
        ),
        migrations.CreateModel(
            name='WorkType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(blank=True, null=True, verbose_name='Code')),
                ('name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Name')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated')),
            ],
            options={
                'verbose_name': 'WorkType',
                'verbose_name_plural': 'WorkType',
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(verbose_name='Code')),
                ('name', models.CharField(blank=True, max_length=10, null=True, verbose_name='Name')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated')),
                ('type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='surveys18.ProductType', verbose_name='Product Type')),
            ],
            options={
                'verbose_name': 'Unit',
                'verbose_name_plural': 'Unit',
            },
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('farmer_id', models.CharField(max_length=12, verbose_name='Farmer Id')),
                ('farmer_name', models.CharField(blank=True, max_length=10, null=True, verbose_name='Name')),
                ('total_pages', models.IntegerField(verbose_name='Total Pages')),
                ('page', models.IntegerField(verbose_name='Page')),
                ('origin_class', models.IntegerField(blank=True, null=True, verbose_name='Origin Class')),
                ('hire', models.BooleanField(default=False, verbose_name='Hire')),
                ('non_hire', models.BooleanField(default=False, verbose_name='Non Hire')),
                ('note', models.TextField(blank=True, null=True, verbose_name='Note')),
                ('is_updated', models.BooleanField(default=False, verbose_name='Is Updated')),
                ('readonly', models.BooleanField(default=True, verbose_name='Read Only')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Investigation Date')),
                ('distance', models.IntegerField(blank=True, null=True, verbose_name='Investigation Distance(km)')),
                ('period', models.IntegerField(blank=True, null=True, verbose_name='Investigation Period')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated')),
                ('investigator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='surveys18', to=settings.AUTH_USER_MODEL, verbose_name='Investigator')),
                ('lacks', models.ManyToManyField(blank=True, related_name='surveys18', to='surveys18.Lack', verbose_name='Lack')),
                ('management_types', models.ManyToManyField(blank=True, related_name='surveys', to='surveys18.ManagementType', verbose_name='Management Types')),
            ],
            options={
                'verbose_name': 'Survey',
                'verbose_name_plural': 'Survey',
            },
        ),
        migrations.CreateModel(
            name='Subsidy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('has_subsidy', models.BooleanField(default=False, verbose_name='Has Subsidy')),
                ('none_subsidy', models.BooleanField(default=False, verbose_name='None Subsidy')),
                ('count', models.IntegerField(blank=True, null=True, verbose_name='Number Of People')),
                ('month_delta', models.IntegerField(blank=True, null=True, verbose_name='Month Delta')),
                ('day_delta', models.IntegerField(blank=True, null=True, verbose_name='Day Delta')),
                ('hour_delta', models.IntegerField(blank=True, null=True, verbose_name='Hour Delta')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated')),
                ('survey', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='subsidy', to='surveys18.Survey', verbose_name='Survey')),
            ],
            options={
                'verbose_name': 'Subsidy',
                'verbose_name_plural': 'Subsidy',
            },
        ),
        migrations.CreateModel(
            name='ShortTermLack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(blank=True, null=True, verbose_name='Number Of People')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated')),
                ('months', models.ManyToManyField(blank=True, related_name='short_term_lacks', to='surveys18.Month', verbose_name='Months')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='short_term_lacks', to='surveys18.Product', verbose_name='Product')),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='short_term_lacks', to='surveys18.Survey', verbose_name='Survey')),
                ('work_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='short_term_lacks', to='surveys18.WorkType', verbose_name='Work Type')),
            ],
            options={
                'verbose_name': 'ShortTermLack',
                'verbose_name_plural': 'ShortTermLack',
            },
        ),
        migrations.CreateModel(
            name='ShortTermHire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avg_work_day', models.FloatField(blank=True, null=True, verbose_name='Average Work Day')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated')),
                ('month', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='surveys18.Month', verbose_name='Month')),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='short_term_hires', to='surveys18.Survey', verbose_name='Survey')),
                ('work_types', models.ManyToManyField(blank=True, related_name='short_term_hires', to='surveys18.WorkType', verbose_name='Work Types')),
            ],
            options={
                'verbose_name': 'ShortTermHire',
                'verbose_name_plural': 'ShortTermHire',
                'ordering': ('month',),
            },
        ),
        migrations.CreateModel(
            name='Refuse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extra', models.CharField(blank=True, max_length=100, null=True, verbose_name='Extra')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated')),
                ('reason', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='refuse', to='surveys18.RefuseReason', verbose_name='Refuse')),
                ('subsidy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='refuses', to='surveys18.Subsidy', verbose_name='Subsidy')),
            ],
            options={
                'verbose_name': 'Refuse',
                'verbose_name_plural': 'Refuse',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='surveys18.ProductType', verbose_name='Product Type'),
        ),
        migrations.CreateModel(
            name='PopulationAge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(blank=True, null=True, verbose_name='Count')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated')),
                ('age_scope', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='surveys18.AgeScope', verbose_name='Age Scope')),
                ('gender', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='surveys18.Gender', verbose_name='Gender')),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='population_ages', to='surveys18.Survey', verbose_name='Survey')),
            ],
            options={
                'verbose_name': 'PopulationAge',
                'verbose_name_plural': 'PopulationAge',
            },
        ),
        migrations.CreateModel(
            name='Population',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth_year', models.IntegerField(blank=True, null=True, verbose_name='Birth Year')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated')),
                ('education_level', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='education_level', to='surveys18.EducationLevel', verbose_name='Education Level')),
                ('farmer_work_day', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='farmer_work_day', to='surveys18.FarmerWorkDay', verbose_name='Farmer Work Day')),
                ('gender', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='relationship', to='surveys18.Gender', verbose_name='Gender')),
                ('life_style', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='life_style', to='surveys18.LifeStyle', verbose_name='Life Style')),
                ('other_farm_work', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='other_farm_work', to='surveys18.OtherFarmWork', verbose_name='Other Farm Work')),
                ('relationship', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='relationship', to='surveys18.Relationship', verbose_name='Relationship')),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='populations', to='surveys18.Survey', verbose_name='Survey')),
            ],
            options={
                'verbose_name': 'Population',
                'verbose_name_plural': 'Population',
                'ordering': ('id', 'relationship'),
            },
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=100, null=True, verbose_name='Phone')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated')),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phones', to='surveys18.Survey', verbose_name='Survey')),
            ],
            options={
                'verbose_name': 'Phone',
                'verbose_name_plural': 'Phone',
            },
        ),
        migrations.CreateModel(
            name='NumberWorkers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('count', models.IntegerField(blank=True, null=True, verbose_name='Count')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated')),
                ('age_scope', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='number_workers', to='surveys18.AgeScope', verbose_name='Age Scope')),
                ('content_type', models.ForeignKey(limit_choices_to=models.Q(models.Q(('app_label', 'surveys18'), ('model', 'longtermhire')), models.Q(('app_label', 'surveys18'), ('model', 'shorttermhire')), _connector='OR'), on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name': 'NumberWorkers',
                'verbose_name_plural': 'NumberWorkers',
            },
        ),
        migrations.CreateModel(
            name='NoSalaryHire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(blank=True, null=True, verbose_name='Number Of People')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated')),
                ('month', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='surveys18.Month', verbose_name='Month')),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='no_salary_hires', to='surveys18.Survey', verbose_name='Survey')),
            ],
            options={
                'verbose_name': 'NoSalaryHire',
                'verbose_name_plural': 'NoSalaryHire',
                'ordering': ('month',),
            },
        ),
        migrations.CreateModel(
            name='Loss',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(verbose_name='Code')),
                ('name', models.CharField(blank=True, max_length=10, null=True, verbose_name='Name')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated')),
                ('type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='surveys18.ProductType', verbose_name='Product Type')),
            ],
            options={
                'verbose_name': 'Loss',
                'verbose_name_plural': 'Loss',
            },
        ),
        migrations.CreateModel(
            name='LongTermLack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(blank=True, null=True, verbose_name='Number Of People')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated')),
                ('months', models.ManyToManyField(blank=True, related_name='long_term_lacks', to='surveys18.Month', verbose_name='Months')),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='long_term_lacks', to='surveys18.Survey', verbose_name='Survey')),
                ('work_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='long_term_lacks', to='surveys18.WorkType', verbose_name='Work Type')),
            ],
            options={
                'verbose_name': 'LongTermLack',
                'verbose_name_plural': 'LongTermLack',
            },
        ),
        migrations.CreateModel(
            name='LongTermHire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avg_work_day', models.FloatField(blank=True, null=True, verbose_name='Average Work Day')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated')),
                ('months', models.ManyToManyField(blank=True, related_name='long_term_hires', to='surveys18.Month', verbose_name='Months')),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='long_term_hires', to='surveys18.Survey', verbose_name='Survey')),
                ('work_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='long_term_hires', to='surveys18.WorkType', verbose_name='Work Type')),
            ],
            options={
                'verbose_name': 'LongTermHire',
                'verbose_name_plural': 'LongTermHire',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='LivestockMarketing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raising_number', models.IntegerField(blank=True, null=True, verbose_name='Raising Number')),
                ('total_yield', models.IntegerField(blank=True, null=True, verbose_name='Total Yield')),
                ('unit_price', models.IntegerField(blank=True, null=True, verbose_name='Unit Price')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated')),
                ('contract', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contract', to='surveys18.Contract', verbose_name='Contract')),
                ('loss', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='livestock_marketing_loss', to='surveys18.Loss', verbose_name='Loss')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='livestock_marketing_product', to='surveys18.Product', verbose_name='Product')),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='livestock_marketings', to='surveys18.Survey', verbose_name='Survey')),
                ('unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='livestock_marketing_unit', to='surveys18.Unit', verbose_name='Unit')),
            ],
            options={
                'verbose_name': 'LivestockMarketing',
                'verbose_name_plural': 'LivestockMarketing',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='LandType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True, verbose_name='Name')),
                ('has_land', models.BooleanField(default=True, verbose_name='Has Land')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated')),
                ('statuses', models.ManyToManyField(blank=True, related_name='land_type', to='surveys18.LandStatus', verbose_name='Land Statuses')),
                ('unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='land_type', to='surveys18.Unit', verbose_name='Unit')),
            ],
            options={
                'verbose_name': 'LandType',
                'verbose_name_plural': 'LandType',
            },
        ),
        migrations.CreateModel(
            name='LandArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(blank=True, null=True, verbose_name='Area Value')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated')),
                ('status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='land_areas', to='surveys18.LandStatus', verbose_name='Status')),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='land_areas', to='surveys18.Survey', verbose_name='Survey')),
                ('type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='land_areas', to='surveys18.LandType', verbose_name='Type')),
            ],
            options={
                'verbose_name': 'LandArea',
                'verbose_name_plural': 'LandArea',
            },
        ),
        migrations.CreateModel(
            name='CropMarketing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('land_number', models.IntegerField(blank=True, null=True, verbose_name='Land Number')),
                ('land_area', models.IntegerField(blank=True, null=True, verbose_name='Land Area')),
                ('plant_times', models.IntegerField(blank=True, null=True, verbose_name='Plant Times')),
                ('total_yield', models.IntegerField(blank=True, null=True, verbose_name='Total Yield')),
                ('unit_price', models.IntegerField(blank=True, null=True, verbose_name='Unit Price')),
                ('has_facility', models.IntegerField(blank=True, choices=[(0, 'No'), (1, 'Yes')], null=True, verbose_name='Has Facility')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated')),
                ('loss', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='crop_marketing_loss', to='surveys18.Loss', verbose_name='Loss')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='surveys18.Product', verbose_name='Product Code')),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='crop_marketings', to='surveys18.Survey', verbose_name='Survey')),
                ('unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='crop_marketing_unit', to='surveys18.Unit', verbose_name='Unit')),
            ],
            options={
                'verbose_name': 'CropMarketing',
                'verbose_name_plural': 'CropMarketing',
                'ordering': ('id', 'land_number'),
            },
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extra', models.CharField(blank=True, max_length=50, null=True, verbose_name='Extra')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated')),
                ('farm_related_business', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='business', to='surveys18.FarmRelatedBusiness', verbose_name='Farm Related Business')),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='businesses', to='surveys18.Survey', verbose_name='Survey')),
            ],
        ),
        migrations.CreateModel(
            name='BuilderFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Create Time')),
                ('token', models.TextField(blank=True, null=True, verbose_name='Token String')),
                ('datafile', models.FileField(blank=True, null=True, upload_to='surveys18/builders/', verbose_name='DataFile')),
                ('type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='surveys18.BuilderFileType', verbose_name='BuilderFileType')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='files', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'BuilderFile',
                'verbose_name_plural': 'BuilderFile',
            },
        ),
        migrations.CreateModel(
            name='AnnualIncome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated')),
                ('income_range', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='surveys18.IncomeRange', verbose_name='Income Range')),
                ('market_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='surveys18.MarketType', verbose_name='Market Type')),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='annual_incomes', to='surveys18.Survey', verbose_name='Survey')),
            ],
            options={
                'verbose_name': 'AnnualIncome',
                'verbose_name_plural': 'AnnualIncomes',
            },
        ),
        migrations.CreateModel(
            name='AddressMatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match', models.BooleanField(default=False, verbose_name='Address Match')),
                ('mismatch', models.BooleanField(default=False, verbose_name='Address MisMatch')),
                ('address', models.CharField(blank=True, max_length=100, null=True, verbose_name='Address')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated')),
                ('survey', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='address_match', to='surveys18.Survey', verbose_name='Survey')),
            ],
            options={
                'verbose_name': 'AddressMatch',
                'verbose_name_plural': 'AddressMatch',
            },
        ),
    ]
