"""
Mobile Responsive Fix Script
Applies comprehensive mobile responsive fixes to home2.html, event-details.html, and schedule.html
"""

# Replacement patterns for speaker cards (lines 360-420 in home2.html)
speaker_card_fixes = [
    # Pattern 1: Card padding
    ('p-6 shadow-xl border-2 border-transparent hover:border-rose-300', 'p-4 sm:p-5 lg:p-6 shadow-xl border-2 border-transparent hover:border-rose-300'),
    ('p-6 shadow-xl border-2 border-transparent hover:border-cyan-300', 'p-4 sm:p-5 lg:p-6 shadow-xl border-2 border-transparent hover:border-cyan-300'),
    ('p-6 shadow-xl border-2 border-transparent hover:border-amber-300', 'p-4 sm:p-5 lg:p-6 shadow-xl border-2 border-transparent hover:border-amber-300'),
    ('p-6 shadow-xl border-2 border-transparent hover:border-lime-300', 'p-4 sm:p-5 lg:p-6 shadow-xl border-2 border-transparent hover:border-lime-300'),
]

# Stats section fixes
stats_section_fixes = {
    'section_padding': 'py-12 sm:py-20 lg:py-32',
    'container_padding': 'px-4 sm:px-6 lg:px-8',
    'header_mb': 'mb-10 sm:mb-16 lg:mb-20',
    'grid': 'gap-4 sm:gap-6 lg:gap-8 grid-cols-1 sm:grid-cols-2 lg:grid-cols-4',
    'card_padding': 'p-6 sm:p-8 lg:p-10',
    'icon_size': 'text-3xl sm:text-4xl lg:text-5xl',
    'number_size': 'text-4xl sm:text-6xl lg:text-8xl',
    'label_size': 'text-base sm:text-lg lg:text-xl',
}

# Testimonials section fixes  
testimonials_fixes = {
    'section_padding': 'py-12 sm:py-20 lg:py-32',
    'grid': 'gap-5 sm:gap-6 lg:gap-8 md:grid-cols-2 lg:grid-cols-3',
    'card_padding': 'p-5 sm:p-6 lg:p-8',
    'quote_icon': 'text-2xl sm:text-3xl lg:text-4xl',
    'quote_text': 'text-sm sm:text-base',
    'star_size': 'text-base sm:text-lg lg:text-xl',
    'name_size': 'text-base sm:text-lg',
    'role_size': 'text-xs sm:text-sm',
}

# CTA section fixes
cta_fixes = {
    'section_padding': 'py-12 sm:py-20 lg:py-32',
    'button_padding': 'px-6 sm:px-8 py-4 sm:py-5',
    'button_text': 'text-base sm:text-lg',
}

print("Mobile Responsive Fix Patterns Defined")
print(f"Speaker card fixes: {len(speaker_card_fixes)} patterns")
print(f"Stats section: {len(stats_section_fixes)} properties")
print(f"Testimonials: {len(testimonials_fixes)} properties")
print(f"CTA: {len(cta_fixes)} properties")
print("\nUse these patterns with multi_replace_string_in_file tool")
