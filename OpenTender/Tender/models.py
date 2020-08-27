from django.db import models

class USER(models.Model):
    user_id = models.AutoField(auto_created=True, primary_key=True)
    Email = models.CharField(max_length=50)
    Phone_No = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)
    Confirm_Password = models.CharField(max_length=50)
    Company_name = models.CharField(max_length=50)

    class Meta:
        db_table = "user_data"

class POST(models.Model):
    post_id = models.AutoField(auto_created=True, primary_key=True)
    Tender_Name = models.CharField(max_length=50)
    Status = models.CharField(max_length=50)
    Date = models.DateField()
    Tender_Type = models.CharField(max_length=50)
    Business_Scale = models.CharField(max_length=50)
    Entry_Fee = models.IntegerField()
    Rules_Regulation = models.CharField(max_length=500)
    Tender_Image = models.ImageField(default="img.jpg")
    objects = models.Manager()

    class Meta:
        db_table = "post_data"

class APPLY(models.Model):
    apply_id = models.AutoField(auto_created=True, primary_key=True)
    Email = models.CharField(max_length=50)
    Company_Name = models.CharField(max_length=50)
    Phone_no = models.IntegerField()
    Address = models.CharField(max_length=50)
    CV_file = models.FileField(default="cv.doc")
    uses_id = models.ForeignKey(USER,default=1, on_delete=models.CASCADE)
    post_id = models.ForeignKey(POST,default=1, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "apply_data"