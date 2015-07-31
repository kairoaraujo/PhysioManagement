# -*- coding: utf-8 -*-

from gluon.tools import Crud

@auth.requires_membership('admin')
def index():
    return dict(title = "Gerência")


@auth.requires_membership('admin')
def list_all():

    all_people = db(db.person.id>0).select(orderby=db.person.name)

    return dict(title = "Lista de Contatos", all_people = all_people)


@auth.requires_membership('admin')
def list_patients():

    # on db, the patient is ID 5
    all_patients = db(db.person.type_person==2).select(orderby=db.person.name)
    return dict(title = "Lista de Pacientes", all_patients = all_patients)


@auth.requires_membership('admin')
def details():

    patient     = db(db.person.id == request.args(0)).select()
    treatments  = db(db.treatment.patient == request.args(0)).select()
    attendments = db(db.attendance.patient == request.args(0)).select()



    return dict(title = "Paciente", patient=patient, treatments=treatments,
            attendments=attendments)


@auth.requires_membership('admin')
def new_treatment():
    db.treatment.patient.default = request.args(0)
    db.treatment.patient.writable = db.treatment.patient.readable = False
    form = SQLFORM(db.treatment, submit_button='Adicionar',
            labels={
                #'patient':'Paciente',
                'treatment':'Tratamento',
                'diagnosis':'Diagnóstico',
                'pathologies':'Patologias',
                'medications':'Medicamentos',
                'start_date':'Data início',
                }
            )

    if form.process().accepted:
        response.flash = 'Contato cadastrado!'
    elif form.errors:
        response.flash = 'Erro ao cadastrar! Verifique os dados.'

    return dict(title='Novo tratamento', form=form)


@auth.requires_membership('admin')
def new_person():
    form = SQLFORM(db.person, submit_button='Salvar',
            labels={'name':'Nome Completo',
            'born':'Data de Nascimento',
            'address':'Endereço',
            'phone':'Telefone',
            'mobile':'Celular',
            'other_phone':'Telefone (outro)',
            'doc_type':'Tipo de Documento',
            'doc_id':'Número do documento',
            'type_person':'Tipo Cadastro',
            'health_care':'Plano de Saúde',
            'doctor':'Médico ',
            'doctor_doc':'CRM do Médico',
            'name_responsable':'[Responsável] Nome',
            'born_responsable':'[Responsável] Data Nascimento',
            'phone_responsable':'[Responsável] Telefone',
            'mobile_responsable':'[Responsável] Celular',
            'email_responsable':'[Responsável] E-mail',
            'address_responsable':'[Responsável] Endereço',
            'doc_type_responsable':'[Responsável] Tipo documento (N/A se no existir responsável)',
            'doc_id_responsable':'[Responsável] Número documento',
            'notes':'Anotacoes diversas'}
                )
    if form.process().accepted:
        response.flash = 'Contato cadastrado!'
    elif form.errors:
        response.flash = 'Erro ao cadastrar! Verifique os dados.'
    return dict(title='Cadastro', form=form)


@auth.requires_membership('admin')
def new_attendance():
    db.attendance.patient.default = request.args(0)
    db.attendance.patient.writable = db.attendance.patient.readable = False
    db.attendance.treatment.default = request.args(1)
    db.attendance.treatment.writable = db.attendance.treatment.readable = False

    form = SQLFORM(db.attendance, submit_button='Adicionar',
            labels={
                #'patient':'Paciente',
                #'treatment':'Tratamento',
                'care_date':'Data de atendimento',
                'pa_start':'PA Inicial',
                'spo2_start':'SPO2 Inicial',
                'bpm_start':'BPM Inicial',
                'pa_end':'PA Final',
                'spo_end':'SPO2 Final',
                'bpm_end':'BPM Final',
                'patient_owner':'Fisioterapeuta',
                'notes':'Observações:'
                }
            )

    if form.process().accepted:
        response.flash = 'Contato cadastrado!'
    elif form.errors:
        response.flash = 'Erro ao cadastrar! Verifique os dados.'

    return dict(title='Novo tratamento', form=form)


@auth.requires_membership('admin')
def update_person():
    crud = Crud(globals(), db)
    form = crud.update(db.person, request.args(0),
            labels={'name':'Nome Completo',
            'born':'Data de Nascimento',
            'address':'Endereço',
            'phone':'Telefone',
            'mobile':'Celular',
            'other_phone':'Telefone (outro)',
            'doc_type':'Tipo de Documento',
            'doc_id':'Número do documento',
            'type_person':'Tipo Cadastro',
            'health_care':'Plano de Saúde',
            'doctor':'Médico ',
            'doctor_doc':'CRM do Médico',
            'name_responsable':'[Responsável] Nome',
            'born_responsable':'[Responsável] Data Nascimento',
            'phone_responsable':'[Responsável] Telefone',
            'mobile_responsable':'[Responsável] Celular',
            'email_responsable':'[Responsável] E-mail',
            'address_responsable':'[Responsável] Endereço',
            'doc_type_responsable':'[Responsável] Tipo documento (N/A se no existir responsável)',
            'doc_id_responsable':'[Responsável] Número documento',
            'notes':'Anotacoes diversas'}
            )
    return dict(title="Atualizar cadastro", form=form)


@auth.requires_membership('admin')
def update_treatment():
    crud = Crud(globals(), db)
    db.treatment.patient.writable = db.treatment.patient.readable = False
    form = crud.update(db.treatment, request.args(0),
            labels={
                #'patient':'Paciente',
                'treatment':'Tratamento',
                'diagnosis':'Diagnóstico',
                'pathologies':'Patologias',
                'medications':'Medicamentos',
                'start_date':'Data início',
                }
            )
    return dict(title="Atualizar tratamento", form=form)


@auth.requires_membership('admin')
def update_attendance():
    crud = Crud(globals(), db)
    db.attendance.patient.default = request.args(0)
    db.attendance.patient.writable = db.attendance.patient.readable = False
    db.attendance.treatment.default = request.args(1)
    db.attendance.treatment.writable = db.attendance.treatment.readable = False

    form = crud.update(db.attendance, request.args(0),
            labels={
                #'patient':'Paciente',
                #'treatment':'Tratamento',
                'care_date':'Data de atendimento',
                'pa_start':'PA Inicial',
                'spo2_start':'SPO2 Inicial',
                'bpm_start':'BPM Inicial',
                'pa_end':'PA Final',
                'spo_end':'SPO2 Final',
                'bpm_end':'BPM Final',
                'patient_owner':'Fisioterapeuta',
		'conduct':'Conduta',
                'notes':'Observações:'
                }
            )

    return dict(title='Atualizar tratamento', form=form)

