from django.shortcuts import render
from django.db.models import Manager
import sys
from django.http import HttpResponse
from resumes.models import *
from django.template import RequestContext, loader
from django.db import connection


# A function organizing the info requested on the resume page
def resume(request, resume_id):
    template = loader.get_template('resumes/resume.html')
    our_resume = Resume.objects.get(pk=resume_id)
    our_skills = Skills.objects.raw("SELECT * from resumes_skills where resume_id = %s", [resume_id])
    our_education = EdHistory.objects.raw(
        "SELECT * from resumes_edhistory where resume_id = %s", [resume_id])
    our_jobs = JobHistory.objects.raw(
        "SELECT * from resumes_jobhistory where resume_id = %s", [resume_id])
    our_references = References.objects.raw(
        "SELECT * from resumes_references where resume_id = %s", [resume_id])
    context = RequestContext(request, {
        'resume': our_resume,
        'skills': our_skills,
        'jobs': our_jobs,
        'education': our_education,
        'references': our_references})

    return HttpResponse(template.render(context))


# A function to control the work done when requesting the search page
def search(request):

    fname = request.GET.get('fname')
    lname = request.GET.get('lname')
    skill = request.GET.get('skill')

    # some mild regex work here so we ignore empty search boxes in our query
    if fname == "":
        fname = "%"

    if lname == "":
        lname = "%"

    if skill == "":
        skill = "%"

    # gets the database connection
    cursor = connection.cursor()
    cursor.execute(
        'SELECT DISTINCT r.id, r.low_salary, r.high_salary, r.title from resumes_resume r' +
        ' INNER JOIN resumes_applicant a ON r.applicant_id = a.id ' +
        ' INNER JOIN resumes_skills s ON r.id = s.resume_id' +
        ' WHERE a.lname LIKE %s AND a.fname LIKE %s and s.skill LIKE %s', [lname, fname, skill])

    # puts everything into the resume object to send to the search page
    resumes = cursor.fetchall()
    template = loader.get_template('resumes/search.html')
    context = RequestContext(request, {'resumes': resumes})
    return HttpResponse(template.render(context))


def start(request):
    return HttpResponse("Start or search a resume")

