import django
import csv, sys, os
from datetime import *

django_project  = "C:/Users/Nichola/MScProjects/Django_groupwork/"
sys.path.append(django_project)
os.environ['DJANGO_SETTINGS_MODULE'] ='mysite.settings'

import django
django.setup()
from BRCA_VarDb.models import *

csv_filename = "C:/Users/Nichola/MScProjects/Django_groupwork/BRCA_VarDb/BRCA1_variants.csv"
data = csv.reader(open(csv_filename), delimiter=',')

#For each row in the csv file, instantiate the django models 
#and fill models with columns from each row.
for row in data:
	if row[0] !='Name':
		datenow= datetime.datetime.now()
		patient=Patient()
		name = str(row[0])
		patient.forename = name.split()[0]
		patient.surname= name.split()[1]
		patient.reg_date= datenow
		patient.save()
			
		occurance = Occurance()
		occurance.patient_id=patient
		occurance.stage = row[2]
		occurance.description = row[3]
		occurance.age_at_occurance = row[1]
		occurance.occ_date=datenow
		occurance.save()
					
		investigation = Investigation()
		investigation.occurance_id=occurance
		investigation.sequencer = row[4]
		investigation.inv_date='2018-02-01'
		investigation.save()
		
		gene = Gene()
		gene.investigation_id=investigation
		gene.gene_name = row[9]
		gene.save()
	
		transcript = Transcript()
		transcript.gene_id=gene
		transcript.refseq_id = row[10]
		transcript.save()
			
		variant=Variant()
		variant.transcript_id = transcript
		variant.cdna_variant = row[5]
		variant.protein_variant = row[6]
		variant.genomic_variant = row[7]
		if row[8] == "":
			variant.pathogenicity = 0
		else:
			variant.pathogenicity = row[8]
		variant.save()
		
	
	