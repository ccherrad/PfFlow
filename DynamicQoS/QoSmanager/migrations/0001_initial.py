# Generated by Django 2.0.4 on 2019-07-09 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Access',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('management_interface', models.CharField(max_length=45)),
                ('management_address', models.CharField(max_length=45)),
                ('username', models.CharField(max_length=45)),
                ('password', models.CharField(max_length=45)),
                ('enable_secret', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('match', models.CharField(max_length=45)),
                ('app_priority', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], max_length=20)),
                ('drop_prob', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], max_length=20)),
                ('dscp_value', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='BusinessApp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('match', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='BusinessType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=45)),
                ('management', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='QoSmanager.Access')),
            ],
        ),
        migrations.CreateModel(
            name='Dscp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority', models.CharField(max_length=45)),
                ('drop_prob', models.CharField(max_length=45)),
                ('drop_min', models.CharField(max_length=45)),
                ('drop_max', models.CharField(max_length=45)),
                ('denominator', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Interface',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interface_name', models.CharField(max_length=45)),
                ('interface_address', models.CharField(max_length=45)),
                ('interface_prefixlen', models.IntegerField()),
                ('interface_speed', models.IntegerField()),
                ('ingress', models.BooleanField(default=True)),
                ('device', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='QoSmanager.Device')),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_speed', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Policing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cir', models.CharField(max_length=45)),
                ('pir', models.CharField(max_length=45)),
                ('dscp_transmit', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='PolicyIn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('description', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='PolicyOut',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('description', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='RegroupementClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('priority', models.CharField(max_length=45)),
                ('bandwidth', models.CharField(max_length=45)),
                ('policing', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='QoSmanager.Policing')),
                ('policy_out', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='QoSmanager.PolicyOut')),
            ],
        ),
        migrations.CreateModel(
            name='Topology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topology_name', models.CharField(max_length=45)),
                ('topology_desc', models.CharField(max_length=45)),
            ],
        ),
        migrations.AddField(
            model_name='link',
            name='topology_ref',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='QoSmanager.Topology'),
        ),
        migrations.AddField(
            model_name='dscp',
            name='regroupement_class',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='QoSmanager.RegroupementClass'),
        ),
        migrations.AddField(
            model_name='device',
            name='topology_ref',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='QoSmanager.Topology'),
        ),
        migrations.AddField(
            model_name='businessapp',
            name='business_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='QoSmanager.BusinessType'),
        ),
        migrations.AddField(
            model_name='application',
            name='business_app',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='QoSmanager.BusinessApp'),
        ),
        migrations.AddField(
            model_name='application',
            name='business_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='QoSmanager.BusinessType'),
        ),
        migrations.AddField(
            model_name='application',
            name='dscp',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='QoSmanager.Dscp'),
        ),
        migrations.AddField(
            model_name='application',
            name='policy_in',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='QoSmanager.PolicyIn'),
        ),
        migrations.AddField(
            model_name='application',
            name='regroupement_class',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='QoSmanager.RegroupementClass'),
        ),
    ]
