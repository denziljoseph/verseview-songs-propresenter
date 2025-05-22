import uuid
from typing import List
from jinja2 import Template
import templates.template_text as tt


def render_lines(lines: List[str], first_line_template: Template, additional_line_template: Template) -> str:
    """Render RTF/notes data from lines with appropriate templates."""
    rendered = [
        first_line_template.render(verseview_lyrics2_line=lines[0]).strip()
    ] if lines else []

    for line in lines[1:]:
        rendered.append(
            additional_line_template.render(verseview_lyrics2_line=line).strip()
        )

    return "".join(rendered)

def render_notes(lines: List[str], first_line_template: Template, additional_line_template: Template) -> str:
    """Render notes section from lines."""
    rendered = [
        first_line_template.render(verseview_lyrics_line=lines[0]).strip()
    ] if lines else []

    for line in lines[1:]:
        rendered.append(
            additional_line_template.render(verseview_lyrics_line=line).strip()
        )

    return "".join(rendered)

def generate_template(df):
    """Generates song templates from a DataFrame."""
    templates = {
        'cue_groups': Template(tt.cue_groups_template),
        'cues': Template(tt.cues_template),
        'base_slide_data': Template(tt.base_slide_rtf_data_template),
        'base_first_line': Template(tt.base_slide_rtf_first_line_template),
        'base_additional_line': Template(tt.base_slide_rtf_additional_line_template),
        'notes_data': Template(tt.notes_rtf_data_template),
        'notes_first_line': Template(tt.notes_first_line_template),
        'notes_additional_line': Template(tt.notes_additional_line_template),
        'main': Template(tt.main_template),
    }

    for _, row in df.iterrows():
        song_guid = uuid.uuid4()
        song_name = row['name']

        cue_groups_str = ''
        cues_str = ''

        for i in range(row['lyrics_verses_count']):
            # Generate GUIDs
            verse_guid = uuid.uuid4()
            cue_group_guid = uuid.uuid4()
            actions_guid = uuid.uuid4()
            element1_guid = uuid.uuid4()
            element2_guid = uuid.uuid4()
            presentation_guid = uuid.uuid4()

            # Slide RTF content
            lyrics_lines = row['list_lyrics2'][i].split('<BR>')
            rtf_data = templates['base_slide_data'].render(
                first_line_template=render_lines(lyrics_lines, templates['base_first_line'], templates['base_additional_line']),
                additional_line_template=""
            )

            # Notes RTF content
            notes_lines = row['list_lyrics'][i].split('<BR>')
            notes_data = templates['notes_data'].render(
                first_line_template=render_notes(notes_lines, templates['notes_first_line'], templates['notes_additional_line']),
                additional_line_template=""
            )

            cue_groups_str += templates['cue_groups'].render(
                cue_group_guid=cue_group_guid,
                verse_guid=verse_guid
            ) + "\n"

            cues_str += templates['cues'].render(
                verse_guid=verse_guid,
                actions_guid=actions_guid,
                element1_guid=element1_guid,
                element2_guid=element2_guid,
                base_slide_rtf_data_template=rtf_data,
                presentation_guid=presentation_guid,
                notes_rtf_data_template=notes_data
            ) + "\n"

        # Final song template
        main_rendered = templates['main'].render(
            song_guid=song_guid,
            song_name=song_name,
            arrangement_guid=uuid.uuid4(),
            intro_guid=uuid.uuid4(),
            outro_guid=uuid.uuid4(),
            intro_group_guid=uuid.uuid4(),
            outro_group_guid=uuid.uuid4(),
            cue_groups_template=cue_groups_str.strip(),
            cues_template=cues_str.strip()
        )

        yield {
                    "song_name": song_name,
                    "song_guid": song_guid,
                    "rendered_template": main_rendered
                }

