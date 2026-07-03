"""
Django Admin configuration for the portfolio.

Features:
- Custom admin header and branding
- Inline image previews
- List filters, search, and ordering
- Publication tabs by status
- Rich list displays
"""

from django.contrib import admin
from django.utils.html import format_html
from .models import (
    Profile, ImpactStat, Publication, Project,
    Skill, LeadershipRole, Award
)


# ──────────────────────────────────────────────
#  PROFILE ADMIN
# ──────────────────────────────────────────────
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    fieldsets = (
        ('🧑 Identity', {
            'fields': ('name', 'title', 'tagline', 'canonical_url', 'twitter_handle'),
        }),
        ('📊 Stats', {
            'fields': ('cgpa', 'papers_count'),
        }),
        ('📝 About Section', {
            'fields': ('about_quote', 'about_body_1', 'about_body_2', 'research_tags'),
        }),
        ('🎓 Education', {
            'fields': (
                'edu_current_institution', 'edu_degree', 'edu_period',
                'edu_hsc_institution', 'edu_hsc_degree', 'edu_hsc_period', 'edu_hsc_gpa',
            ),
        }),
        ('📬 Contact & Social', {
            'fields': ('email', 'linkedin_url', 'github_url', 'orcid_url', 'facebook_url'),
        }),
        ('💬 Contact Section Text', {
            'fields': ('availability_text', 'contact_headline', 'contact_sub'),
        }),
    )

    def has_add_permission(self, request):
        """Allow only one profile."""
        return not Profile.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


# ──────────────────────────────────────────────
#  IMPACT STATS ADMIN
# ──────────────────────────────────────────────
@admin.register(ImpactStat)
class ImpactStatAdmin(admin.ModelAdmin):
    list_display = ('order', 'value', 'label', 'is_accent', 'data_count', 'is_decimal')
    list_editable = ('order', 'is_accent', 'is_decimal')
    list_display_links = ('value',)
    ordering = ('order',)


# ──────────────────────────────────────────────
#  PUBLICATION ADMIN
# ──────────────────────────────────────────────
@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = (
        'display_index', 'status_badge', 'short_title', 'venue_short', 'year', 'order'
    )
    list_display_links = ('short_title',)
    list_filter = ('status', 'year')
    search_fields = ('title', 'authors', 'venue')
    list_editable = ('order',)
    ordering = ('status', 'order')

    fieldsets = (
        ('Publication Info', {
            'fields': (
                'title', 'authors', 'venue', 'year',
                'status', 'display_index', 'order',
            ),
        }),
        ('BibTeX Citation', {
            'fields': ('bibtex_key', 'bibtex_entry'),
            'classes': ('collapse',),
        }),
    )

    def status_badge(self, obj):
        colours = {
            'accepted': ('#22c55e', '#0a2710'),
            'review': ('#eab308', '#1a1400'),
            'ongoing': ('#818cf8', '#0f0f1f'),
        }
        fg, bg = colours.get(obj.status, ('#999', '#111'))
        return format_html(
            '<span style="background:{};color:{};padding:2px 10px;border-radius:999px;'
            'font-size:11px;font-weight:600;text-transform:uppercase">{}</span>',
            bg, fg, obj.get_status_display()
        )
    status_badge.short_description = 'Status'
    status_badge.allow_tags = True

    def short_title(self, obj):
        return obj.title[:70] + ('…' if len(obj.title) > 70 else '')
    short_title.short_description = 'Title'

    def venue_short(self, obj):
        return obj.venue[:40] + ('…' if len(obj.venue) > 40 else '')
    venue_short.short_description = 'Venue'


# ──────────────────────────────────────────────
#  PROJECT ADMIN
# ──────────────────────────────────────────────
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('order', 'icon_emoji', 'title', 'layout_badge', 'badge_type', 'url_link', 'order')
    list_display_links = ('title',)
    list_editable = ('order',)
    list_filter = ('layout', 'badge_type')
    search_fields = ('title', 'description')
    ordering = ('order',)

    fieldsets = (
        ('Project Details', {
            'fields': ('title', 'description', 'url', 'icon_emoji', 'order'),
        }),
        ('Display Options', {
            'fields': ('layout', 'badge_type', 'badge_label', 'tags'),
        }),
    )

    def layout_badge(self, obj):
        colours = {
            'handbook': ('#818cf8', '#0f0f1f'),
            'featured': ('#eab308', '#1a1400'),
            'normal': ('#999', '#111'),
        }
        fg, bg = colours.get(obj.layout, ('#999', '#111'))
        return format_html(
            '<span style="background:{};color:{};padding:2px 8px;border-radius:999px;font-size:11px">{}</span>',
            bg, fg, obj.get_layout_display()
        )
    layout_badge.short_description = 'Layout'

    def url_link(self, obj):
        return format_html('<a href="{}" target="_blank">↗ Open</a>', obj.url)
    url_link.short_description = 'URL'


# ──────────────────────────────────────────────
#  SKILL ADMIN
# ──────────────────────────────────────────────
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('order', 'name', 'row', 'is_highlighted', 'highlighted_pill')
    list_display_links = ('name',)
    list_editable = ('order', 'is_highlighted')
    list_filter = ('row', 'is_highlighted')
    ordering = ('row', 'order')

    def highlighted_pill(self, obj):
        if obj.is_highlighted:
            return format_html(
                '<span style="background:rgba(99,102,241,0.15);color:#818cf8;'
                'padding:2px 10px;border-radius:999px;font-size:11px">✦ Accent</span>'
            )
        return format_html(
            '<span style="color:#555;font-size:11px">Normal</span>'
        )
    highlighted_pill.short_description = 'Style'

    # Make is_highlighted editable directly in list
    def get_list_editable(self, request):
        return ('order', 'is_highlighted')


# ──────────────────────────────────────────────
#  LEADERSHIP ROLE ADMIN
# ──────────────────────────────────────────────
@admin.register(LeadershipRole)
class LeadershipRoleAdmin(admin.ModelAdmin):
    list_display = ('order', 'role', 'organization', 'is_current')
    list_editable = ('order', 'is_current')
    list_display_links = ('role',)
    ordering = ('order',)


# ──────────────────────────────────────────────
#  AWARD ADMIN
# ──────────────────────────────────────────────
@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    list_display = ('order', 'icon_emoji', 'title', 'eyebrow', 'is_featured')
    list_editable = ('order', 'is_featured')
    list_display_links = ('title',)
    ordering = ('order',)
