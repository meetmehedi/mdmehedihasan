"""Views for the portfolio."""
from django.shortcuts import render
from .models import Profile, ImpactStat, Publication, Project, Skill, LeadershipRole, Award


def index(request):
    """Main portfolio page."""
    profile = Profile.objects.first()
    impact_stats = ImpactStat.objects.all()
    accepted_pubs = Publication.objects.filter(status='accepted').order_by('order')
    review_pubs = Publication.objects.filter(status='review').order_by('order')
    ongoing_pubs = Publication.objects.filter(status='ongoing').order_by('order')
    projects = Project.objects.all()
    skills_row1 = Skill.objects.filter(row=1).order_by('order')
    skills_row2 = Skill.objects.filter(row=2).order_by('order')
    leadership_roles = LeadershipRole.objects.all()
    awards = Award.objects.all()
    featured_award = awards.filter(is_featured=True).first()

    # Build BibTeX dict for JavaScript
    bib_entries = {}
    for pub in Publication.objects.exclude(bibtex_key='').exclude(bibtex_entry=''):
        bib_entries[pub.bibtex_key] = pub.bibtex_entry

    context = {
        'profile': profile,
        'impact_stats': impact_stats,
        'accepted_pubs': accepted_pubs,
        'review_pubs': review_pubs,
        'ongoing_pubs': ongoing_pubs,
        'projects': projects,
        'skills_row1': skills_row1,
        'skills_row2': skills_row2,
        'leadership_roles': leadership_roles,
        'awards': awards,
        'featured_award': featured_award,
        'bib_entries': bib_entries,
    }
    return render(request, 'core/index.html', context)
