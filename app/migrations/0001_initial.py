# Generated by Django 4.2 on 2023-04-12 13:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('selling_price', models.FloatField()),
                ('discounted_price', models.FloatField()),
                ('description', models.TextField()),
                ('inclusions', models.TextField(default='')),
                ('category', models.CharField(choices=[('MS', 'Music-Sheets'), ('MI', 'Musical-Instruments'), ('EQ', 'Equipment')], max_length=2)),
                ('product_image', models.ImageField(upload_to='product')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('razorpay_order_id', models.CharField(blank=True, max_length=100, null=True)),
                ('razorpay_payment_status', models.CharField(blank=True, max_length=100, null=True)),
                ('razorpay_payment_id', models.CharField(blank=True, max_length=100, null=True)),
                ('paid', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('locality', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('mobile', models.IntegerField(default=0)),
                ('zipcode', models.IntegerField()),
                ('state', models.CharField(choices=[('Abra', 'Abra'), ('Agusan del Norte', 'Agusan del Norte'), ('Agusan del Sur', 'Agusan del Sur'), ('Aklan', 'Aklan'), ('Albay', 'Albay'), ('Antique', 'Antique'), ('Apayao', 'Apayao'), ('Aurora', 'Aurora'), ('Agusan del Sur', 'Agusan del Sur'), ('Basilan', 'Basilan'), ('Bataan', 'Bataan'), ('Batanes', 'Batanes'), ('Batangas', 'Batangas'), ('Benguet', 'Benguet'), ('Biliran', 'Biliran'), ('Bohol', 'Bohol'), ('Bukidnon', 'Bukidnon'), ('Bulacan', 'Bulacan'), ('Cagayan', 'Cagayan'), ('Camarines Norte', 'Camarines Norte'), ('Camarines Sur', 'Camarines Sur'), ('Camiguin', 'Camiguin'), ('Capiz', 'Capiz'), ('Catanduanes', 'Catanduanes'), ('Cavite', 'Cavite'), ('Cebu', 'Cebu'), ('Davao Occidental', 'Davao Occidental'), ('Davao Oriental', 'Davao Oriental'), ('Davao de Oro', 'Davao de Oro'), ('Davao del Norte', 'Davao del Norte'), ('Davao del Sur', 'Davao del Sur'), ('Dinagat Islands', 'Dinagat Islands'), ('Eastern Samar', 'Eastern Samar'), ('Guimaras', 'Guimaras'), ('Ifugao', 'Ifugao'), ('Ilocos Norte', 'Ilocos Norte'), ('Ilocos Sur', 'Ilocos Sur'), ('Iloilo', 'Iloilo'), ('Isabela', 'Isabela'), ('Kalinga', 'Kalinga'), ('La Union', 'La Union'), ('Laguna', 'Laguna'), ('Lanao del Norte', 'Lanao del Norte'), ('Lanao del Sur', 'Lanao del Norte'), ('Leyte', 'Leyte'), ('Maguindanao', 'Maguindanao'), ('Marinduque', 'Marinduque'), ('Masbate', 'Masbate'), ('Misamis Occidental', 'Misamis Occidental'), ('Misamis Oriental', 'Misamis Oriental'), ('Mountain Province', 'Mountain Province'), ('Negros Occidental', 'Negros Occidental'), ('Negros Oriental', 'Negros Oriental'), ('North Cotabato', 'North Cotabato'), ('Northern Samar', 'Northern Samar'), ('Nueva Ecija', 'Nueva Ecija'), ('Nueva Vizcaya', 'Nueva Vizcaya'), ('Occidental Mindoro', 'Occidental Mindoro'), ('Oriental Mindoro', 'Oriental Mindoro'), ('Palawan', 'Palawan'), ('Pampanga', 'Pampanga'), ('Pangasinan', 'Pangasinan'), ('Quezon', 'Quezon'), ('Quirino', 'Quirino'), ('Rizal', 'Rizal'), ('Romblon', 'Romblon'), ('Samar', 'Samar'), ('Sarangani', 'Sarangani'), ('Siquijor', 'Siquijor'), ('Sorsogon', 'Sorsogon'), ('South Cotabato', 'South Cotabato'), ('Southern Leyte', 'Southern Leyte'), ('Sultan Kudarat', 'Sultan Kudarat'), ('Sulu', 'Sulu'), ('Surigao del Norte', 'Surigao del Norte'), ('Surigao del Sur', 'Surigao del Sur'), ('Tarlac', 'Tarlac'), ('Tawi-Tawi', 'Tawi-Tawi'), ('Zamboanga Sibugay', 'Zamboanga Sibugay'), ('Zamboanga del Norte', 'Zamboanga del Norte'), ('Zamboanga del Sur', 'Zamboanga del Sur')], max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
