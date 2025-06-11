from django.db import models

class graveyard(models.Model):
    graveyard_id=models.AutoField(primary_key=True)
    graveyard_name=models.CharField(max_length=30)
    graveyard_add=models.CharField(max_length=50)
    graveyard_city=models.CharField(max_length=15)
    graveyard_plots=models.IntegerField()
    graveyard_phoneno=models.CharField(max_length=15)
    graveyard_column=models.IntegerField()
    graveyard_row=models.IntegerField()
   

    def __str__(self):
        return str(self.graveyard_id)
    
class graveplots(models.Model):
    grave_id=models.AutoField(primary_key=True)
    grave_no=models.CharField(max_length=20)
    status=models.CharField(max_length=10 ,choices=[('buried','buried'),('reserved','reserved'),('available','available')])
    graveyard_id=models.ForeignKey(graveyard, on_delete=models.CASCADE)
    grave_column=models.CharField(max_length=10)
    grave_row=models.IntegerField()


    def __str__(self):
        return str(self.grave_id)
    
class deceased(models.Model):
    deceased_id=models.AutoField(primary_key=True)
    deceased_name=models.CharField(max_length=30)
    deceased_dob=models.DateField()
    deceased_dod=models.DateField()
    deceased_add=models.TextField(max_length=100)
    deceased_phoneno=models.CharField(max_length=15)
    deceased_info=models.TextField(max_length=200)
    grave_id=models.ForeignKey(graveplots, on_delete=models.CASCADE)                         
                         
    def __str__(self):
        return str(self.deceased_id)

class booking(models.Model):
    booking_id=models.AutoField(primary_key=True)
    booking_date=models.DateField(auto_now=True)
    booking_reserver_name=models.CharField(max_length=20)
    booking_reserver_contact=models.CharField(max_length=20)
    booking_proof=models.CharField(max_length=20)
    booking_status=models.CharField(max_length=10,choices=[('pending','pending'),('reserved','reserved')])
    booking_grave_id=models.ForeignKey(graveplots,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.booking_id)

class maintain(models.Model):
    main_id=models.AutoField(primary_key=True)
    main_date=models.DateField(auto_now_add=True)
    main_name=models.CharField(max_length=20)
    main_contact=models.CharField(max_length=15)
    main_completebydate=models.DateField()
    main_status=models.CharField(max_length=10,choices=[('pending','pending'),('completed','completed')])    
    main_grave_id=models.ForeignKey(graveplots,on_delete=models.CASCADE)
    main_disc=models.TextField(max_length=200)

    def __str__(self):
        return str(self.main_id)
    
class digital_memorial(models.Model):
    memorial_id=models.AutoField(primary_key=True)
    memorial_name=models.CharField(max_length=30)
    memorial_message=models.TextField(max_length=200)
    
    memorial_deceased_id=models.ForeignKey(deceased,on_delete=models.CASCADE)

    def  __str__(self):
        return str(self.memorial_id)
    
class employee(models.Model):
    employee_id=models.AutoField(primary_key=True)
    employee_name=models.CharField(max_length=20)
    employee_add=models.TextField(max_length=100)
    employee_no=models.CharField(max_length=15)
    employee_work_at=models.ForeignKey(graveyard,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.employee_id)
    

class performed_by(models.Model):
    employee_id=models.ForeignKey(employee,on_delete=models.CASCADE)
    main_id=models.ForeignKey(maintain,on_delete=models.CASCADE)
    completed_at=models.DateField()

    def __str__(self):
        return str(self.main_id)
    
class contact(models.Model):
    graveyard_id=models.ForeignKey(graveyard,on_delete=models.CASCADE)
    contact=models.CharField(max_length=50)
     
    def __str__(self):
        return str(self.contact)
