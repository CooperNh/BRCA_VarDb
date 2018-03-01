from django.http import HttpResponse
from .models import *
from django.shortcuts import render, render_to_response
from django.template import loader


patient_list = []
# def index(request):
	# data = Patient.objects.values('forename')	
	# all_data=Patient.objects.all()
	# #for patient in data:
		# #patient_list.append(patient)
	# template = loader.get_template("BRCA_VarDb/patients.html")
	# context = {'data':data}		
	# return HttpResponse(template.render(context, request))

def index(request):
	data = Patient.objects.all()
	return render(request, 'BRCA_VarDb/patients.html', locals())
	
	
	
	
	
	
	
# SELECT BRCA_VarDb_patient.forename, 
# BRCA_VarDb_patient.surname, 
# BRCA_VarDb_occurance.stage, 
# BRCA_VarDb_occurance.description, 
# BRCA_VarDb_occurance.age_at_occurance,
# BRCA_VarDb_investigation.sequencer,
# BRCA_VarDb_gene.gene_name, 
# BRCA_VarDb_transcript.refseq_id, 
# BRCA_VarDb_variant.cdna_variant, 
# BRCA_VarDb_variant.protein_variant,
# BRCA_VarDb_variant.genomic_variant, 
# BRCA_VarDb_variant.pathogenicity
# FROM BRCA_VarDb_patient
# LEFT JOIN BRCA_VarDb_occurance on BRCA_VarDb_patient.id =BRCA_VarDb_occurance.patient_id_id 
# LEFT JOIN BRCA_VarDb_investigation on BRCA_VarDb_occurance.id = BRCA_VarDb_investigation.occurance_id_id 
# LEFT JOIN BRCA_VarDb_gene on BRCA_VarDb_investigation.id = BRCA_VarDb_gene.investigation_id_id
# LEFT JOIN BRCA_VarDb_transcript on BRCA_VarDb_gene.id = BRCA_VarDb_transcript.gene_id_id
# LEFT JOIN BRCA_VarDb_variant on BRCA_VarDb_transcript.id = BRCA_VarDb_variant.transcript_id_id 