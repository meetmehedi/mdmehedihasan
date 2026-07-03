"""
Models for the portfolio CMS.

All content is manageable via Django Admin:
- Profile        → personal info, photo, CV
- ImpactStat     → the 3 big numbers in the impact bar
- Publication    → research papers (accepted / review / ongoing)
- Project        → bento grid cards
- Skill          → marquee pills (two rows)
- LeadershipRole → role entries inside the leadership card
- Award          → the featured award card (NASA etc.)
"""

from django.db import models


# ──────────────────────────────────────────────
#  PROFILE  (singleton – only one row expected)
# ──────────────────────────────────────────────
class Profile(models.Model):
    name = models.CharField(max_length=200, default="Md. Mehedi Hasan")
    title = models.CharField(
        max_length=300,
        default="AI & ML Researcher · NASA International Space Apps Champion 2025 · IEEE Member"
    )
    tagline = models.TextField(
        default=(
            "Building interpretable machine learning systems at the intersection of "
            "behavioral modeling, social engineering detection, and socio-technical resilience."
        )
    )
    about_quote = models.TextField(
        default=(
            "I work at the intersection of AI, behavioral modeling, and socio-technical "
            "resilience building systems that are not only accurate but explainable and "
            "grounded in human reality."
        )
    )
    about_body_1 = models.TextField(
        default=(
            "I'm a BSc Computer Science & Engineering student at Dhaka International "
            "University (CGPA 3.76 / 4.00), graduating December 2027. My research focuses "
            "on detecting social engineering through interpretable behavioral anomaly modeling, "
            "predicting system failures using socio-economic and IoT data, and building "
            "continual learning frameworks for dynamic environments."
        )
    )
    about_body_2 = models.TextField(
        default=(
            "As President of DIU Computer Programming Club and an active IEEE & IEEE Computer "
            "Society Member, I combine research depth with community leadership championed by "
            "a NASA Space Apps 2025 victory with Team Polaris."
        )
    )
    email = models.EmailField(default="meetmehedi1@gmail.com")
    linkedin_url = models.URLField(default="https://www.linkedin.com/in/meetmehedi")
    github_url = models.URLField(default="https://github.com/meetmehedi")
    orcid_url = models.URLField(default="https://orcid.org/0009-0006-1427-8769")
    facebook_url = models.URLField(default="https://www.facebook.com/meetmehedi1/")
    twitter_handle = models.CharField(max_length=100, default="@meetmehedi")
    canonical_url = models.URLField(default="https://www.mdmehedihasan.us/")
    cgpa = models.CharField(max_length=20, default="3.76")
    papers_count = models.CharField(max_length=20, default="8+")

    # About card stats
    edu_current_institution = models.CharField(
        max_length=200, default="Dhaka International University"
    )
    edu_degree = models.CharField(
        max_length=200, default="B.Sc. Computer Science & Engineering"
    )
    edu_period = models.CharField(max_length=100, default="Sep 2023 – Dec 2027")
    edu_hsc_institution = models.CharField(
        max_length=200, default="BAF Shaheen College Jashore"
    )
    edu_hsc_degree = models.CharField(
        max_length=200, default="Higher Secondary Certificate (HSC)"
    )
    edu_hsc_period = models.CharField(max_length=100, default="Sep 2020 – Dec 2022")
    edu_hsc_gpa = models.CharField(max_length=20, default="4.75 / 5.00")

    # Research areas tags (comma-separated)
    research_tags = models.TextField(
        default="Behavioral ML,Social Engineering Detection,Interpretable AI,Socio-Economic Modeling,Continual Learning,Geospatial Risk,Computer Vision,LLMs & GenAI"
    )

    # Availability status badge
    availability_text = models.CharField(
        max_length=200, default="Open for Research Collaborations"
    )
    contact_headline = models.CharField(max_length=200, default="Let's Shape the Future")
    contact_sub = models.TextField(
        default=(
            "Open for research collaborations, engineering challenges, or just a friendly "
            "conversation about AI and its impact on humanity."
        )
    )

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profile"

    def __str__(self):
        return self.name

    def get_research_tags_list(self):
        return [t.strip() for t in self.research_tags.split(',') if t.strip()]


# ──────────────────────────────────────────────
#  IMPACT STATS  (the 3 big numbers)
# ──────────────────────────────────────────────
class ImpactStat(models.Model):
    label = models.CharField(max_length=100)
    value = models.CharField(max_length=100, help_text="e.g. '3.76', '8+', '🏆 NASA'")
    is_accent = models.BooleanField(
        default=False, help_text="Use accent colour for value"
    )
    data_count = models.CharField(
        max_length=50, blank=True,
        help_text="Numeric target for count-up animation (leave blank for emoji values)"
    )
    is_decimal = models.BooleanField(default=False, help_text="Use decimal count-up (e.g. 3.76)")
    custom_font_size = models.CharField(
        max_length=100, blank=True,
        help_text="Override font-size inline style (e.g. clamp(32px,5vw,48px))"
    )
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "Impact Stat"
        verbose_name_plural = "Impact Stats"

    def __str__(self):
        return f"{self.value} — {self.label}"


# ──────────────────────────────────────────────
#  PUBLICATION
# ──────────────────────────────────────────────
class Publication(models.Model):
    STATUS_CHOICES = [
        ('accepted', 'Accepted'),
        ('review', 'Under Review'),
        ('ongoing', 'Ongoing'),
    ]
    INDEX_CHOICES = [
        ('01', '01'), ('02', '02'), ('03', '03'), ('04', '04'),
        ('05', '05'), ('06', '06'), ('07', '07'), ('08', '08'),
        ('R1', 'R1'), ('R2', 'R2'), ('R3', 'R3'), ('R4', 'R4'),
        ('R5', 'R5'), ('R6', 'R6'), ('R7', 'R7'), ('R8', 'R8'),
        ('R9', 'R9'), ('R10', 'R10'), ('R11', 'R11'), ('R12', 'R12'),
        ('O1', 'O1'), ('O2', 'O2'), ('O3', 'O3'),
    ]

    title = models.TextField()
    authors = models.TextField(
        help_text="Use 'Hasan, M. M.' for self — will be bolded automatically"
    )
    venue = models.CharField(max_length=300, blank=True)
    year = models.PositiveSmallIntegerField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='accepted')
    display_index = models.CharField(
        max_length=10, default='01',
        help_text="Display label e.g. 01, R1, O1"
    )
    bibtex_key = models.SlugField(
        max_length=100, blank=True,
        help_text="JavaScript key for BibTeX copy (e.g. hasan2025socio)"
    )
    bibtex_entry = models.TextField(
        blank=True, help_text="Full BibTeX entry"
    )
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['status', 'order']
        verbose_name = "Publication"
        verbose_name_plural = "Publications"

    def __str__(self):
        return self.title[:80]


# ──────────────────────────────────────────────
#  PROJECT
# ──────────────────────────────────────────────
class Project(models.Model):
    LAYOUT_CHOICES = [
        ('normal', 'Normal (1 col)'),
        ('featured', 'Featured (2 cols)'),
        ('handbook', 'Handbook (full width)'),
    ]
    BADGE_TYPE_CHOICES = [
        ('nasa', '🏆 NASA Winner'),
        ('research', '📖 Research'),
        ('none', 'None'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField()
    icon_emoji = models.CharField(max_length=10, blank=True, help_text="e.g. 🌍 🤖 ⚡")
    badge_type = models.CharField(
        max_length=20, choices=BADGE_TYPE_CHOICES, default='none'
    )
    badge_label = models.CharField(max_length=100, blank=True, help_text="Override badge text")
    tags = models.CharField(
        max_length=500, blank=True,
        help_text="Comma-separated tags e.g. NASA API,Three.js,Machine Learning"
    )
    layout = models.CharField(max_length=20, choices=LAYOUT_CHOICES, default='normal')
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.title

    def get_tags_list(self):
        return [t.strip() for t in self.tags.split(',') if t.strip()]

    def get_badge_display_label(self):
        if self.badge_label:
            return self.badge_label
        badge_labels = {
            'nasa': '🏆 NASA Winner',
            'research': '📖 Handbook',
        }
        return badge_labels.get(self.badge_type, '')


# ──────────────────────────────────────────────
#  SKILL  (marquee pills)
# ──────────────────────────────────────────────
class Skill(models.Model):
    ROW_CHOICES = [
        (1, 'Row 1 (left → right)'),
        (2, 'Row 2 (right → left)'),
    ]
    name = models.CharField(max_length=100)
    is_highlighted = models.BooleanField(
        default=False, help_text="Accent colour pill"
    )
    row = models.PositiveSmallIntegerField(choices=ROW_CHOICES, default=1)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['row', 'order']
        verbose_name = "Skill"
        verbose_name_plural = "Skills"

    def __str__(self):
        return self.name


# ──────────────────────────────────────────────
#  LEADERSHIP ROLE
# ──────────────────────────────────────────────
class LeadershipRole(models.Model):
    role = models.CharField(max_length=200)
    organization = models.CharField(max_length=300)
    is_current = models.BooleanField(default=True, help_text="Show accent dot for current roles")
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "Leadership Role"
        verbose_name_plural = "Leadership Roles"

    def __str__(self):
        return f"{self.role} @ {self.organization}"


# ──────────────────────────────────────────────
#  AWARD
# ──────────────────────────────────────────────
class Award(models.Model):
    eyebrow = models.CharField(max_length=200)
    title = models.CharField(max_length=300)
    description = models.TextField()
    icon_emoji = models.CharField(max_length=10, default="🏆")
    tags = models.CharField(
        max_length=500, blank=True,
        help_text="Comma-separated tags"
    )
    is_featured = models.BooleanField(
        default=True, help_text="Show as wide featured card"
    )
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "Award"
        verbose_name_plural = "Awards"

    def __str__(self):
        return self.title

    def get_tags_list(self):
        return [t.strip() for t in self.tags.split(',') if t.strip()]
