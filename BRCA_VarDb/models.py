from django.db import models
import datetime
# Create your models here.

class Patient(models.Model):
	#p_id
	forename = models.CharField(max_length=200)
	surname = models.CharField(max_length=200)
	reg_date = models.DateTimeField()
	
	def __str__(self):
		return self.id, self.forename, self.surname, self.reg_date
	
class Occurance(models.Model):
	#o_id
	patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
	stage = models.IntegerField()
	description = models.CharField(max_length=200)
	age_at_occurance = models.IntegerField()
	occ_date = models.DateTimeField()
	
	def __str__(self):
		return self.patient_id, self.stage, self.description, self.age_at_occurance, self.occ_date
	
class Investigation(models.Model):
	#i_id
	occurance_id = models.ForeignKey(Occurance, on_delete=models.CASCADE)
	sequencer = models.CharField(max_length=200)
	inv_date = models.DateTimeField()
	
	def __str__(self):
		return self.occurance_id, self.sequencer, self.inv_date
		
		
class Gene(models.Model):
	#g_id
	investigation_id = models.ForeignKey(Investigation, on_delete=models.CASCADE)
	gene_name = models.CharField(max_length=200)
		
	def __str__(self):
		return self.investigation_id, self.gene_name
	
class Transcript(models.Model):
	gene_id = models.ForeignKey(Gene, on_delete=models.CASCADE)
	refseq_id = models.CharField(max_length=200)
	
	def __str__(self):
		return self.gene_id, self.refseq_id
	
class Variant(models.Model):
	#v_id
	transcript_id = models.ForeignKey(Transcript, on_delete=models.CASCADE)
	cdna_variant = models.CharField(max_length=200)
	protein_variant = models.CharField(max_length=200)
	genomic_variant = models.CharField(max_length=200)
	pathogenicity = models.IntegerField(default = 0, blank =True,null=True)
		
	def __str__(self):
		return self.transcript_id, self.cdna_variant, self.protein_variant, self.genomic_variant, self.pathogenicity
	