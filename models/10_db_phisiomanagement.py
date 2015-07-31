'''
Default table PhysionManagement
'''

db.define_table('type_person',
	Field('type_person', 'string')
)

db.define_table('doc_type',
        Field('doc_type', 'string')
)

db.define_table('person',
	Field('name','string'),
    Field('born','datetime', requires=[IS_NOT_EMPTY(error_message= 'Campo obrigatório'),
        IS_DATE(format='%d-%m-%Y', error_message='Formato DD-MM-AAAA. Ex: 10-07-1981')]),
	Field('address','string'),
	Field('phone','string', requires=IS_NOT_EMPTY(error_message= 'Campo obrigatório')),
	Field('mobile','string', requires=IS_NOT_EMPTY(error_message= 'Campo obrigatório')),
	Field('other_phone','string'),
	Field('email','string'),
	#Field('doc_type','string'),
    Field('doc_type', 'reference doc_type', requires=IS_IN_DB(db, db.doc_type.id, '%(doc_type)s', error_message= 'Campo obrigatório')),
	Field('doc_id','string'),
	#Field('type_person','reference type_person'),
    Field('type_person', 'reference type_person', requires=IS_IN_DB(db, db.type_person.id, '%(type_person)s',error_message= 'Campo obrigatório')),
	Field('health_care','string'),
    Field('doctor','string'),
    Field('doctor_doc','string'),
    Field('name_responsable', 'string'),
    Field('born_responsable', 'datetime', requires=IS_DATE(format='%d-%m-%Y', error_message='Formato DD-MM-AAAA. Ex: 10-07-1981')),
    Field('address_responsable', 'string'),
    Field('phone_responsable', 'string'),
    Field('mobile_responsable', 'string'),
    Field('email_responsable', 'string'),
    Field('doc_type_responsable', 'reference doc_type', requires=IS_IN_DB(db, db.doc_type.id, '%(doc_type)s', error_message= 'Campo obrigatório')),
    Field('doc_id_responsable', 'string'),
	Field('notes','text', 'length=1024')
)
db.define_table('treatment',
    Field('patient', 'reference person', requires=IS_IN_DB(db, db.person.id, '%(name)s',error_message= 'Campo obrigatório')),
    Field('treatment','string'),
	Field('diagnosis','string'),
	Field('pathologies','string'),
	Field('medications','text'),
    Field('start_date','datetime', requires=IS_DATE(format='%d-%m-%Y', error_message='Formato DD-MM-AAAA. Ex: 10-07-1981')),
)

# get only fisioterapeutas
query_fisio=db(db.person.type_person==1)

db.define_table('attendance',
    Field('patient','reference person', requires=IS_IN_DB(db, db.person.id, '%(name)s',error_message= 'Campo obrigatório')),
	Field('treatment','reference treatment', requires=IS_IN_DB(db, db.treatment.id, '%(treatment)s',error_message= 'Campo obrigatório')),
    Field('care_date','datetime', requires=IS_DATE(format='%d-%m-%Y', error_message='Formato DD-MM-AAAA. Ex: 10-07-1981')),
	Field('pa_start','string'),
	Field('spo2_start','string'),
	Field('bpm_start','string'),
	Field('pa_end','string'),
	Field('spo_end','string'),
	Field('bpm_end','string'),
	Field('patient_owner','reference person', requires=IS_IN_DB(query_fisio, db.person.id, '%(name)s',error_message= 'Campo obritgário')),
	Field('conduct','text','length=2014'),
	Field('notes','text', 'length=1024')
)

