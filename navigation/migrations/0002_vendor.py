# Generated by Django 3.2 on 2021-06-02 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navigation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vcode', models.CharField(max_length=1000)),
                ('vname', models.CharField(max_length=122)),
                ('vadd', models.CharField(max_length=122)),
                ('city', models.CharField(max_length=122)),
                ('pin', models.CharField(choices=[('1', 'Jammu & Kashmir'), ('2', 'Himachal Pradesh'), ('3', 'Punjab'), ('4', 'Chandigarh'), ('5', 'Uttarakhand'), ('6', 'Haryana'), ('7', 'Delhi'), ('8', 'Rajasthan'), ('9', 'Uttar Pradesh'), ('10', 'Bihar'), ('11', 'Sikkim'), ('12', 'Arunachal Pradesh'), ('13', 'Nagaland'), ('14', 'Manipur'), ('15', 'Mizoram'), ('16', 'Tripura'), ('17', 'Meghalaya'), ('18', 'Assam'), ('19', 'West Bengal'), ('20', 'Jharkhand'), ('21', 'Odisha'), ('22', 'Chattisgarh'), ('23', 'Madhya Pradesh'), ('24', 'Gujarat'), ('25', 'Daman & Diu'), ('26', 'Dadra & Nagar Haveli')], max_length=2)),
            ],
        ),
    ]
