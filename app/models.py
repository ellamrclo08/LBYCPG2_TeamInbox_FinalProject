from django.db import models
from django.contrib.auth.models import User

STATE_CHOICES = (
	('Abra', 'Abra'),
	('Agusan del Norte', 'Agusan del Norte'),
	('Agusan del Sur', 'Agusan del Sur'),
	('Aklan', 'Aklan'),
	('Albay', 'Albay'),
	('Antique', 'Antique'),
	('Apayao', 'Apayao'),
	('Aurora', 'Aurora'),
	('Agusan del Sur', 'Agusan del Sur'),
	('Basilan', 'Basilan'),
	('Bataan', 'Bataan'),
	('Batanes', 'Batanes'),
	('Batangas', 'Batangas'),
	('Benguet', 'Benguet'),
	('Biliran', 'Biliran'),
	('Bohol', 'Bohol'),
	('Bukidnon', 'Bukidnon'),
	('Bulacan', 'Bulacan'),
	('Cagayan', 'Cagayan'),
	('Camarines Norte', 'Camarines Norte'),
	('Camarines Sur', 'Camarines Sur'),
	('Camiguin', 'Camiguin'),
	('Capiz', 'Capiz'),
	('Catanduanes', 'Catanduanes'),
	('Cavite', 'Cavite'),
	('Cebu', 'Cebu'),
	('Davao Occidental', 'Davao Occidental'),
	('Davao Oriental', 'Davao Oriental'),
	('Davao de Oro', 'Davao de Oro'),
	('Davao del Norte', 'Davao del Norte'),
	('Davao del Sur', 'Davao del Sur'),
	('Dinagat Islands', 'Dinagat Islands'),
	('Eastern Samar', 'Eastern Samar'),
	('Guimaras', 'Guimaras'),
	('Ifugao', 'Ifugao'),
	('Ilocos Norte', 'Ilocos Norte'),
	('Ilocos Sur', 'Ilocos Sur'),
	('Iloilo', 'Iloilo'),
	('Isabela', 'Isabela'),
	('Kalinga', 'Kalinga'),
	('La Union', 'La Union'),
	('Laguna', 'Laguna'),
	('Lanao del Norte', 'Lanao del Norte'),
	('Lanao del Sur', 'Lanao del Norte'),
	('Leyte', 'Leyte'),
	('Maguindanao', 'Maguindanao'),
	('Marinduque', 'Marinduque'),
	('Masbate', 'Masbate'),
	('Misamis Occidental', 'Misamis Occidental'),
	('Misamis Oriental', 'Misamis Oriental'),
	('Mountain Province', 'Mountain Province'),
	('Negros Occidental', 'Negros Occidental'),
	('Negros Oriental', 'Negros Oriental'),
	('North Cotabato', 'North Cotabato'),
	('Northern Samar', 'Northern Samar'),
	('Nueva Ecija', 'Nueva Ecija'),
	('Nueva Vizcaya', 'Nueva Vizcaya'),
	('Occidental Mindoro', 'Occidental Mindoro'),
	('Oriental Mindoro', 'Oriental Mindoro'),
	('Palawan', 'Palawan'),
	('Pampanga', 'Pampanga'),
	('Pangasinan', 'Pangasinan'),
	('Quezon', 'Quezon'),
	('Quirino', 'Quirino'),
	('Rizal', 'Rizal'),
	('Romblon', 'Romblon'),
	('Samar', 'Samar'),
	('Sarangani', 'Sarangani'),
	('Siquijor', 'Siquijor'),
	('Sorsogon', 'Sorsogon'),
	('South Cotabato', 'South Cotabato'),
	('Southern Leyte', 'Southern Leyte'),
	('Sultan Kudarat', 'Sultan Kudarat'),
	('Sulu', 'Sulu'),
	('Surigao del Norte', 'Surigao del Norte'),
	('Surigao del Sur', 'Surigao del Sur'),
	('Tarlac', 'Tarlac'),
	('Tawi-Tawi', 'Tawi-Tawi'),
	('Zamboanga Sibugay', 'Zamboanga Sibugay'),
	('Zamboanga del Norte', 'Zamboanga del Norte'),
	('Zamboanga del Sur', 'Zamboanga del Sur'),
)

CATEGORY_CHOICES = (
	('MS', 'Music-Sheets'),
	('MI', 'Musical-Instruments'),
	('EQ', 'Equipment'),
)

class Product(models.Model):
	title = models.CharField(max_length = 100)
	selling_price = models.FloatField()
	discounted_price = models.FloatField()
	description = models.TextField()
	inclusions = models.TextField(default = '')
	category = models.CharField(choices = CATEGORY_CHOICES, max_length = 2)
	product_image = models.ImageField(upload_to = 'product')
	def __str__(self):
		return self.title

class Customer(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	name = models.CharField(max_length = 200)
	locality = models.CharField(max_length = 200)
	city = models.CharField(max_length = 50)
	mobile = models.IntegerField(default = 0)
	zipcode = models.IntegerField()
	state = models.CharField(choices = STATE_CHOICES, max_length = 100)
	def __str__(self):
		return self.name

class Cart(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	product = models.ForeignKey(Product, on_delete = models.CASCADE)
	quantity = models.PositiveIntegerField(default=1)

	@property
	def total_cost(self):
		return self.quantity * self.product.discounted_price
	
STATUS_CHOICES = (
	('Accepted', 'Accepted'),
	('Packed', 'Packed'),
	('On the Way', 'On the Way'),
	('Delivered', 'Delivered'),
	('Cancel', 'Cancel'),
	('Pending', 'Pending'),
)

class Payment(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	amount = models.FloatField()
	razorpay_order_id = models.CharField(max_length = 100, blank = True, null = True)
	razorpay_payment_status = models.CharField(max_length = 100, blank = True, null = True)
	razorpay_payment_id = models.CharField(max_length = 100, blank = True, null = True)
	paid = models.BooleanField(default = False)