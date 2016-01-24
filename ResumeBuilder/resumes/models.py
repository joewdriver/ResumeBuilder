from django.db import models


class Applicant(models.Model):
    email = models.CharField(max_length=100)
    fname = models.CharField(max_length=25)
    lname = models.CharField(max_length=25)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=500)

    def __str__(self):
        return self.fname + " " + self.lname


class Resume(models.Model):
    title = models.CharField(max_length=50)
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    statement = models.CharField(max_length=500)
    low_salary = models.IntegerField(default=10000)
    high_salary = models.IntegerField(default=10000000)

    def __str__(self):
        return self.title


class School(models.Model):
    name = models.CharField(max_length=200)
    website = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class EdHistory(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    start_year = models.IntegerField()
    end_year = models.IntegerField()
    degree_attained = models.CharField(max_length=100)

    def __str__(self):
        return self.degree_attained


class JobHistory(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=50)
    job_description = models.CharField(max_length=500)
    employer = models.CharField(max_length=100)
    start_year = models.IntegerField()
    end_year = models.IntegerField()
    end_salary = models.IntegerField()

    def __str__(self):
        return self.job_title


class Skills(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    skill = models.CharField(max_length=25)

    def __str__(self):
        return self.skill


class References(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    ref_name = models.CharField(max_length=50)
    ref_phone = models.CharField(max_length=15)
    ref_email = models.CharField(max_length=100)
    ref_employer = models.CharField(max_length=50)

    def __str__(self):
        return "reference name: " + self.refname
