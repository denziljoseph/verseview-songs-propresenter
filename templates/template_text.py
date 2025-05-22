cue_groups_template = """cue_groups {
    group {
        uuid {
            string: "{{ cue_group_guid }}"
        }
        name: "Verse"
        color {
            green: 0.466666669
            blue: 0.8
            alpha: 1
        }
        hotKey {
            code: KEY_CODE_ANSI_A
        }
        application_group_identifier {
            string: "ee6fbada-b165-4f90-a9d2-367100e76f17"
        }
        application_group_name: "Verse"
    }
    cue_identifiers {
        string: "{{ verse_guid }}"
    }
}"""
    
cues_template = """cues {
    uuid {
        string: "{{ verse_guid }}"
    }
    completion_target_uuid {
        string: "00000000-0000-0000-0000-000000000000"
    }
    completion_action_type: COMPLETION_ACTION_TYPE_LAST
    completion_action_uuid {
        string: "00000000-0000-0000-0000-000000000000"
    }
    trigger_time {
    }
    actions {
        uuid {
            string: "{{ actions_guid }}"
        }
        isEnabled: true
        type: ACTION_TYPE_PRESENTATION_SLIDE
        slide {
            presentation {
                base_slide {
                    elements {
                        element {
                            uuid {
                                string: "{{ element1_guid }}"
                            }
                            bounds {
                                origin {
                                x: 87.999999999999773
                                y: 540
                                }
                                size {
                                width: 1744.0000000000005
                                height: 443.2871999999993
                                }
                            }
                            opacity: 1
                            locked: true
                            path {
                                closed: true
                                points {
                                    point {
                                    }
                                    q0 {
                                    }
                                    q1 {
                                    }
                                }
                                points {
                                    point {
                                        x: 1
                                    }
                                    q0 {
                                        x: 1
                                    }
                                    q1 {
                                        x: 1
                                    }
                                }
                                points {
                                    point {
                                        x: 1
                                        y: 1
                                    }
                                    q0 {
                                        x: 1
                                        y: 1
                                    }
                                    q1 {
                                        x: 1
                                        y: 1
                                    }
                                }
                                points {
                                    point {
                                        y: 1
                                    }
                                    q0 {
                                        y: 1
                                    }
                                    q1 {
                                        y: 1
                                    }
                                }
                                shape {
                                    type: TYPE_RECTANGLE
                                }
                            }
                            fill {
                                color {
                                    alpha: 0.215686277
                                }
                                enable: true
                            }
                            stroke {
                                width: 3
                                color {
                                    red: 1
                                    green: 1
                                    blue: 1
                                    alpha: 1
                                }
                            }
                            shadow {
                                angle: 315
                                offset: 5
                                radius: 5
                                color {
                                    alpha: 1
                                }
                                opacity: 0.75
                            }
                            feather {
                                radius: 0.65
                                enable: true
                            }
                            text {
                                attributes {
                                    font {
                                        name: "BalooChettan2-ExtraBold"
                                        size: 110
                                        bold: true
                                        family: "BalooChettan2-ExtraBold"
                                        face: "Regular"
                                    }
                                    text_solid_fill {
                                        red: 1
                                        green: 1
                                        blue: 1
                                        alpha: 1
                                    }
                                    paragraph_style {
                                        alignment: ALIGNMENT_CENTER
                                        line_height_multiple: 0.6958333333333333
                                        line_spacing: 1.3
                                        text_list {
                                        }
                                    }
                                    stroke_color {
                                        red: 1
                                        green: 1
                                        blue: 1
                                        alpha: 1
                                    }
                                }
                                shadow {
                                    angle: 315
                                    offset: 5
                                    radius: 5
                                    color {
                                        alpha: 1
                                    }
                                    opacity: 0.75
                                    enable: true
                                }
                                rtf_data: "{\\\\rtf0\\\\ansi\\\\ansicpg1252{\\\\fonttbl\\\\f0\\\\fnil BalooChettan2-ExtraBold;}{\\\\colortbl;\\\\red255\\\\green255\\\\blue255;\\\\red0\\\\green0\\\\blue0;\\\\red255\\\\green255\\\\blue255;}{\\\\*\\\\expandedcolortbl;\\\\csgenericrgb\\\\c100000\\\\c100000\\\\c100000\\\\c100000;\\\\csgenericrgb\\\\c0\\\\c0\\\\c0\\\\c100000;\\\\csgenericrgb\\\\c100000\\\\c100000\\\\c100000\\\\c0;}{\\\\*\\\\listtable}{\\\\*\\\\listoverridetable}\\\\uc1\\\\paperw34880\\\\margl0\\\\margr0\\\\margt0\\\\margb0\\\\pard\\\\li0\\\\fi0\\\\ri0\\\\qc\\\\sb0\\\\sa0\\\\sl167\\\\slmult1\\\\slleading26\\\\f0\\\\b\\\\i0\\\\ul0\\\\strike0\\\\fs220\\\\expnd0\\\\expndtw0\\\\cf1\\\\strokewidth0\\\\strokec2\\\\nosupersub\\\\ulc0\\\\highlight3\\\\cb3}"
                                vertical_alignment: VERTICAL_ALIGNMENT_MIDDLE
                                scale_behavior: SCALE_BEHAVIOR_SCALE_FONT_DOWN
                                margins {
                                }
                                is_superscript_standardized: true
                                transformDelimiter: "  \\342\\200\\242  "
                                chord_pro {
                                    color {
                                        alpha: 1
                                    }
                                }
                            }
                            text_line_mask {
                            }
                        }
                        info: 3
                        data_links {
                            slide_text {
                                source_option: TEXT_SOURCE_OPTION_NOTES
                            }
                        }
                        text_scroller {
                            scroll_rate: 0.5
                            should_repeat: true
                            repeat_distance: 0.057339449541284386
                        }
                    }
                    elements {
                        element {
                            uuid {
                                string: "{{ element2_guid }}"
                            }
                            bounds {
                                origin {
                                    x: 87.999999999999773
                                    y: 52.3333333333336
                                }
                                size {
                                    width: 1744.0000000000005
                                    height: 487.6666666666664
                                }
                            }
                            opacity: 1
                            locked: true
                            path {
                                closed: true
                                points {
                                    point {
                                    }
                                    q0 {
                                    }
                                    q1 {
                                    }
                                }
                                points {
                                    point {
                                        x: 1
                                    }
                                    q0 {
                                        x: 1
                                    }
                                    q1 {
                                        x: 1
                                    }
                                }
                                points {
                                    point {
                                        x: 1
                                        y: 1
                                    }
                                    q0 {
                                        x: 1
                                        y: 1
                                    }
                                    q1 {
                                        x: 1
                                        y: 1
                                    }
                                }
                                points {
                                    point {
                                        y: 1
                                    }
                                    q0 {
                                        y: 1
                                    }
                                    q1 {
                                        y: 1
                                    }
                                }
                                shape {
                                    type: TYPE_RECTANGLE
                                }
                            }
                            fill {
                                color {
                                    alpha: 0.215686277
                                }
                                enable: true
                            }
                            stroke {
                                width: 3
                                color {
                                    red: 1
                                    green: 1
                                    blue: 1
                                    alpha: 1
                                }
                            }
                            shadow {
                                angle: 315
                                offset: 5
                                radius: 5
                                color {
                                    alpha: 1
                                }
                                opacity: 0.75
                            }
                            feather {
                                radius: 0.65
                                enable: true
                            }
                            text {
                                attributes {
                                    font {
                                        name: "BalooChettan2-ExtraBold"
                                        size: 110
                                        bold: true
                                        family: "BalooChettan2-ExtraBold"
                                        face: "Regular"
                                    }
                                    text_solid_fill {
                                        red: 1
                                        green: 1
                                        blue: 1
                                        alpha: 1
                                    }
                                    paragraph_style {
                                        alignment: ALIGNMENT_CENTER
                                        line_height_multiple: 0.6
                                        text_list {
                                        }
                                    }
                                    stroke_color {
                                        red: 1
                                        green: 1
                                        blue: 1
                                        alpha: 1
                                    }
                                }
                                shadow {
                                    angle: 315
                                    offset: 5
                                    radius: 5
                                    color {
                                        alpha: 1
                                    }
                                    opacity: 0.75
                                    enable: true
                                }
                                rtf_data: "{{ base_slide_rtf_data_template }}"
                                vertical_alignment: VERTICAL_ALIGNMENT_MIDDLE
                                scale_behavior: SCALE_BEHAVIOR_SCALE_FONT_DOWN
                                margins {
                                }
                                is_superscript_standardized: true
                                transformDelimiter: "  \\342\\200\\242  "
                                chord_pro {
                                    color {
                                        alpha: 1
                                    }
                                }
                            }
                            text_line_mask {
                            }
                        }
                        info: 3
                        text_scroller {
                            scroll_rate: 0.5
                            should_repeat: true
                            repeat_distance: 0.057339449541284386
                        }
                    }
                    background_color {
                        alpha: 1
                    }
                    size {
                        width: 1920
                        height: 1080
                    }
                    uuid {
                        string: "{{ presentation_guid }}"
                    }
                }
                notes {
                    rtf_data: "{{ notes_rtf_data_template }}"
                    attributes {
                        font {
                            name: "ArialMT"
                            size: 50
                            family: "Arial"
                            face: "Regular"
                        }
                        text_solid_fill {
                            alpha: 1
                        }
                        paragraph_style {
                            line_height_multiple: 1
                            text_list {
                            }
                        }
                        stroke_color {
                            red: 1
                            green: 1
                            blue: 1
                            alpha: 1
                        }
                    }
                }
                chord_chart {
                }
            }
        }
    }
    isEnabled: true
}"""

base_slide_rtf_data_template = """{\\\\rtf0\\\\ansi\\\\ansicpg1252{\\\\fonttbl\\\\f0\\\\fnil BalooChettan2-ExtraBold;}{\\\\colortbl;\\\\red255\\\\green255\\\\blue255;\\\\red0\\\\green0\\\\blue0;\\\\red255\\\\green255\\\\blue255;\\\\red0\\\\green0\\\\blue0;\\\\red0\\\\green0\\\\blue0;\\\\red0\\\\green0\\\\blue0;}{\\\\*\\\\expandedcolortbl;\\\\csgenericrgb\\\\c100000\\\\c100000\\\\c100000\\\\c100000;\\\\csgenericrgb\\\\c0\\\\c0\\\\c0\\\\c100000;\\\\csgenericrgb\\\\c100000\\\\c100000\\\\c100000\\\\c0;\\\\csgenericrgb\\\\c0\\\\c0\\\\c0\\\\c100000;\\\\csgenericrgb\\\\c0\\\\c0\\\\c0\\\\c100000;\\\\csgenericrgb\\\\c0\\\\c0\\\\c0\\\\c100000;}{\\\\*\\\\listtable}{\\\\*\\\\listoverridetable}\\\\uc1\\\\paperw34880\\\\margl0\\\\margr0\\\\margt0\\\\margb0{{ first_line_template }}{{ additional_line_template }}}"""
base_slide_rtf_first_line_template = """\\\\pard\\\\li0\\\\fi0\\\\ri0\\\\qc\\\\sb0\\\\sa0\\\\sl144\\\\slmult1\\\\slleading0\\\\f0\\\\b\\\\i0\\\\ul0\\\\strike0\\\\fs220\\\\expnd0\\\\expndtw0\\\\cf1\\\\strokewidth0\\\\strokec2\\\\nosupersub\\\\ulc0\\\\highlight3\\\\cb3 {{ verseview_lyrics2_line }}"""
base_slide_rtf_additional_line_template = """\\\\par\\\\pard\\\\li0\\\\fi0\\\\ri0\\\\qc\\\\sb0\\\\sa0\\\\sl144\\\\slmult1\\\\slleading0\\\\f0\\\\b\\\\i0\\\\ul0\\\\strike0\\\\fs220\\\\expnd0\\\\expndtw0\\\\cf1\\\\strokewidth0\\\\strokec2\\\\nosupersub\\\\ulc0\\\\highlight3\\\\cb3 {{ verseview_lyrics2_line }}"""

notes_rtf_data_template = """{\\\\rtf0\\\\ansi\\\\ansicpg1252{\\\\fonttbl\\\\f0\\\\fnil ArialMT;}{\\\\colortbl;\\\\red0\\\\green0\\\\blue0;\\\\red255\\\\green255\\\\blue255;\\\\red255\\\\green255\\\\blue255;\\\\red0\\\\green0\\\\blue0;\\\\red0\\\\green0\\\\blue0;\\\\red0\\\\green0\\\\blue0;}{\\\\*\\\\expandedcolortbl;\\\\csgenericrgb\\\\c0\\\\c0\\\\c0\\\\c100000;\\\\csgenericrgb\\\\c100000\\\\c100000\\\\c100000\\\\c100000;\\\\csgenericrgb\\\\c100000\\\\c100000\\\\c100000\\\\c0;\\\\csgenericrgb\\\\c0\\\\c0\\\\c0\\\\c100000;\\\\csgenericrgb\\\\c0\\\\c0\\\\c0\\\\c100000;\\\\csgenericrgb\\\\c0\\\\c0\\\\c0\\\\c100000;}{\\\\*\\\\listtable}{\\\\*\\\\listoverridetable}\\\\uc1\\\\paperw12240\\\\margl0\\\\margr0\\\\margt0\\\\margb0{{ first_line_template }}{{ additional_line_template }}}"""
notes_first_line_template = """\\\\pard\\\\li0\\\\fi0\\\\ri0\\\\ql\\\\sb0\\\\sa0\\\\sl240\\\\slmult1\\\\slleading0\\\\f0\\\\b0\\\\i0\\\\ul0\\\\strike0\\\\fs100\\\\expnd0\\\\expndtw0\\\\cf1\\\\strokewidth0\\\\strokec2\\\\nosupersub\\\\ulc0\\\\highlight3\\\\cb3 {{ verseview_lyrics_line }}"""
notes_additional_line_template = """\\\\par\\\\pard\\\\li0\\\\fi0\\\\ri0\\\\ql\\\\sb0\\\\sa0\\\\sl240\\\\slmult1\\\\slleading0\\\\f0\\\\b0\\\\i0\\\\ul0\\\\strike0\\\\fs100\\\\expnd0\\\\expndtw0\\\\cf1\\\\strokewidth0\\\\strokec2\\\\nosupersub\\\\ulc0\\\\highlight3\\\\cb3 {{ verseview_lyrics_line }}"""


main_template = """application_info {
    platform: PLATFORM_WINDOWS
    platform_version {
        major_version: 10
        patch_version: 4294967295
        build: "22631"
    }
    application: APPLICATION_PROPRESENTER
    application_version {
        major_version: 7
        minor_version: 14
        build: "118358033"
    }
}
uuid {
    string: "{{ song_guid }}"
}
name: "{{ song_name }}"
last_modified_date {
    seconds: 1715498777
}
background {
    color {
        alpha: 1
    }
}
selected_arrangement {
    string: "{{ arrangement_guid }}"
}
cue_groups {
    group {
        uuid {
        string: "{{ intro_group_guid }}"
        }
        name: "Intro"
        color {
        red: 0.701960802
        green: 0.654902
        blue: 0.141176477
        alpha: 1
        }
        hotKey {
        code: KEY_CODE_ANSI_I
        }
        application_group_identifier {
        string: "285e86b5-b939-499d-91d3-7b8796c874b9"
        }
        application_group_name: "Intro"
    }
    cue_identifiers {
        string: "{{ intro_guid }}"
    }
}
{{ cue_groups_template }}
cue_groups {
    group {
        uuid {
        string: "{{ outro_group_guid }}"
        }
        name: "Outro"
        color {
        red: 0.494117647
        green: 0.4627451
        blue: 0.0980392173
        alpha: 1
        }
        hotKey {
        code: KEY_CODE_ANSI_O
        }
        application_group_identifier {
        string: "d7240b2a-c45b-4611-a59a-ef5d0539d53d"
        }
        application_group_name: "Outro"
    }
    cue_identifiers {
        string: "{{ outro_guid }}"
    }
}
cues {
    uuid {
        string: "{{ intro_guid }}"
    }
    name: " 5"
    completion_target_uuid {
        string: "00000000-0000-0000-0000-000000000000"
    }
    completion_action_type: COMPLETION_ACTION_TYPE_LAST
    completion_action_uuid {
        string: "00000000-0000-0000-0000-000000000000"
    }
    trigger_time {
    }
    actions {
        uuid {
        string: "411da0fb-aa57-46de-bfa6-bf7eb491d6a7"
        }
        isEnabled: true
        type: ACTION_TYPE_PRESENTATION_SLIDE
        slide {
        presentation {
            base_slide {
            elements {
                element {
                uuid {
                    string: "8289a16a-d764-4f52-99a9-5d41ef63311c"
                }
                bounds {
                    origin {
                    x: 240
                    y: 135
                    }
                    size {
                    width: 1440
                    height: 810
                    }
                }
                opacity: 1
                path {
                    closed: true
                    points {
                    point {
                    }
                    q0 {
                    }
                    q1 {
                    }
                    }
                    points {
                    point {
                        x: 1
                    }
                    q0 {
                        x: 1
                    }
                    q1 {
                        x: 1
                    }
                    }
                    points {
                    point {
                        x: 1
                        y: 1
                    }
                    q0 {
                        x: 1
                        y: 1
                    }
                    q1 {
                        x: 1
                        y: 1
                    }
                    }
                    points {
                    point {
                        y: 1
                    }
                    q0 {
                        y: 1
                    }
                    q1 {
                        y: 1
                    }
                    }
                    shape {
                    type: TYPE_RECTANGLE
                    }
                }
                fill {
                    color {
                    red: 0.117647059
                    green: 0.564705908
                    blue: 1
                    alpha: 1
                    }
                }
                stroke {
                    width: 3
                    color {
                    red: 1
                    green: 1
                    blue: 1
                    alpha: 1
                    }
                }
                shadow {
                    angle: 315
                    offset: 5
                    radius: 5
                    color {
                    alpha: 1
                    }
                    opacity: 0.75
                }
                feather {
                    radius: 0.05
                }
                text {
                    attributes {
                    font {
                        name: "ArialMT"
                        size: 50
                        family: "Arial"
                        face: "Regular"
                    }
                    text_solid_fill {
                        red: 1
                        green: 1
                        blue: 1
                        alpha: 1
                    }
                    paragraph_style {
                        alignment: ALIGNMENT_CENTER
                        line_height_multiple: 1
                        text_list {
                        }
                    }
                    stroke_color {
                        red: 1
                        green: 1
                        blue: 1
                        alpha: 1
                    }
                    }
                    shadow {
                    angle: 315
                    offset: 5
                    radius: 5
                    color {
                        alpha: 1
                    }
                    opacity: 0.75
                    }
                    rtf_data: "{\\\\rtf0\\\\ansi\\\\ansicpg1252{\\\\fonttbl\\\\f0\\\\fnil ArialMT;}{\\\\colortbl;\\\\red255\\\\green255\\\\blue255;\\\\red255\\\\green255\\\\blue255;}{\\\\*\\\\expandedcolortbl;\\\\csgenericrgb\\\\c100000\\\\c100000\\\\c100000\\\\c100000;\\\\csgenericrgb\\\\c100000\\\\c100000\\\\c100000\\\\c0;}{\\\\*\\\\listtable}{\\\\*\\\\listoverridetable}\\\\uc1\\\\paperw28800\\\\margl0\\\\margr0\\\\margt0\\\\margb0\\\\pard\\\\li0\\\\fi0\\\\ri0\\\\qc\\\\sb0\\\\sa0\\\\sl240\\\\slmult1\\\\slleading0\\\\f0\\\\b0\\\\i0\\\\ul0\\\\strike0\\\\fs100\\\\expnd0\\\\expndtw0\\\\cf1\\\\strokewidth0\\\\strokec1\\\\nosupersub\\\\ulc0\\\\highlight2\\\\cb2}"
                    vertical_alignment: VERTICAL_ALIGNMENT_MIDDLE
                    margins {
                    }
                    is_superscript_standardized: true
                    transformDelimiter: "  \\342\\200\\242  "
                    chord_pro {
                    }
                }
                text_line_mask {
                }
                }
                info: 3
                text_scroller {
                scroll_rate: 0.5
                should_repeat: true
                repeat_distance: 0.069444444444444448
                }
            }
            background_color {
                alpha: 1
            }
            size {
                width: 1920
                height: 1080
            }
            uuid {
                string: "c5d8e83a-d024-47cc-837e-6f5c048a62b8"
            }
            }
            notes {
            rtf_data: "{\\\\rtf0\\\\ansi\\\\ansicpg1252{\\\\fonttbl\\\\f0\\\\fnil ArialMT;}{\\\\colortbl;\\\\red0\\\\green0\\\\blue0;\\\\red255\\\\green255\\\\blue255;\\\\red255\\\\green255\\\\blue255;}{\\\\*\\\\expandedcolortbl;\\\\csgenericrgb\\\\c0\\\\c0\\\\c0\\\\c100000;\\\\csgenericrgb\\\\c100000\\\\c100000\\\\c100000\\\\c100000;\\\\csgenericrgb\\\\c100000\\\\c100000\\\\c100000\\\\c0;}{\\\\*\\\\listtable}{\\\\*\\\\listoverridetable}\\\\uc1\\\\paperw12240\\\\margl0\\\\margr0\\\\margt0\\\\margb0\\\\pard\\\\li0\\\\fi0\\\\ri0\\\\ql\\\\sb0\\\\sa0\\\\sl240\\\\slmult1\\\\slleading0\\\\f0\\\\b0\\\\i0\\\\ul0\\\\strike0\\\\fs100\\\\expnd0\\\\expndtw0\\\\cf1\\\\strokewidth0\\\\strokec2\\\\nosupersub\\\\ulc0\\\\highlight3\\\\cb3}"
            attributes {
                font {
                name: "ArialMT"
                size: 50
                family: "Arial"
                face: "Regular"
                }
                text_solid_fill {
                alpha: 1
                }
                paragraph_style {
                line_height_multiple: 1
                text_list {
                }
                }
                stroke_color {
                red: 1
                green: 1
                blue: 1
                alpha: 1
                }
            }
            }
            chord_chart {
            }
        }
        }
    }
    isEnabled: true
}
{{ cues_template }}
cues {
    uuid {
        string: "{{ outro_guid }}"
    }
    name: " 4"
    completion_target_uuid {
        string: "00000000-0000-0000-0000-000000000000"
    }
    completion_action_type: COMPLETION_ACTION_TYPE_LAST
    completion_action_uuid {
        string: "00000000-0000-0000-0000-000000000000"
    }
    trigger_time {
    }
    actions {
        uuid {
        string: "7be347c9-87e0-4775-80a1-702bb060c916"
        }
        isEnabled: true
        type: ACTION_TYPE_PRESENTATION_SLIDE
        slide {
        presentation {
            base_slide {
            elements {
                element {
                uuid {
                    string: "021f049a-0d59-4c03-8db1-528692314347"
                }
                bounds {
                    origin {
                    x: 240
                    y: 135
                    }
                    size {
                    width: 1440
                    height: 810
                    }
                }
                opacity: 1
                path {
                    closed: true
                    points {
                    point {
                    }
                    q0 {
                    }
                    q1 {
                    }
                    }
                    points {
                    point {
                        x: 1
                    }
                    q0 {
                        x: 1
                    }
                    q1 {
                        x: 1
                    }
                    }
                    points {
                    point {
                        x: 1
                        y: 1
                    }
                    q0 {
                        x: 1
                        y: 1
                    }
                    q1 {
                        x: 1
                        y: 1
                    }
                    }
                    points {
                    point {
                        y: 1
                    }
                    q0 {
                        y: 1
                    }
                    q1 {
                        y: 1
                    }
                    }
                    shape {
                    type: TYPE_RECTANGLE
                    }
                }
                fill {
                    color {
                    red: 0.117647059
                    green: 0.564705908
                    blue: 1
                    alpha: 1
                    }
                }
                stroke {
                    width: 3
                    color {
                    red: 1
                    green: 1
                    blue: 1
                    alpha: 1
                    }
                }
                shadow {
                    angle: 315
                    offset: 5
                    radius: 5
                    color {
                    alpha: 1
                    }
                    opacity: 0.75
                }
                feather {
                    radius: 0.05
                }
                text {
                    attributes {
                    font {
                        name: "ArialMT"
                        size: 50
                        family: "Arial"
                        face: "Regular"
                    }
                    text_solid_fill {
                        red: 1
                        green: 1
                        blue: 1
                        alpha: 1
                    }
                    paragraph_style {
                        alignment: ALIGNMENT_CENTER
                        line_height_multiple: 1
                        text_list {
                        }
                    }
                    stroke_color {
                        red: 1
                        green: 1
                        blue: 1
                        alpha: 1
                    }
                    }
                    shadow {
                    angle: 315
                    offset: 5
                    radius: 5
                    color {
                        alpha: 1
                    }
                    opacity: 0.75
                    }
                    rtf_data: "{\\\\rtf0\\\\ansi\\\\ansicpg1252{\\\\fonttbl\\\\f0\\\\fnil ArialMT;}{\\\\colortbl;\\\\red255\\\\green255\\\\blue255;\\\\red255\\\\green255\\\\blue255;}{\\\\*\\\\expandedcolortbl;\\\\csgenericrgb\\\\c100000\\\\c100000\\\\c100000\\\\c100000;\\\\csgenericrgb\\\\c100000\\\\c100000\\\\c100000\\\\c0;}{\\\\*\\\\listtable}{\\\\*\\\\listoverridetable}\\\\uc1\\\\paperw28800\\\\margl0\\\\margr0\\\\margt0\\\\margb0\\\\pard\\\\li0\\\\fi0\\\\ri0\\\\qc\\\\sb0\\\\sa0\\\\sl240\\\\slmult1\\\\slleading0\\\\f0\\\\b0\\\\i0\\\\ul0\\\\strike0\\\\fs100\\\\expnd0\\\\expndtw0\\\\cf1\\\\strokewidth0\\\\strokec1\\\\nosupersub\\\\ulc0\\\\highlight2\\\\cb2}"
                    vertical_alignment: VERTICAL_ALIGNMENT_MIDDLE
                    margins {
                    }
                    is_superscript_standardized: true
                    transformDelimiter: "  \\342\\200\\242  "
                    chord_pro {
                    }
                }
                text_line_mask {
                }
                }
                info: 3
                text_scroller {
                scroll_rate: 0.5
                should_repeat: true
                repeat_distance: 0.069444444444444448
                }
            }
            background_color {
                alpha: 1
            }
            size {
                width: 1920
                height: 1080
            }
            uuid {
                string: "87e8ad47-06be-44e0-a20a-8e07f1947dc0"
            }
            }
            notes {
            rtf_data: "{\\\\rtf0\\\\ansi\\\\ansicpg1252{\\\\fonttbl\\\\f0\\\\fnil ArialMT;}{\\\\colortbl;\\\\red0\\\\green0\\\\blue0;\\\\red255\\\\green255\\\\blue255;\\\\red255\\\\green255\\\\blue255;}{\\\\*\\\\expandedcolortbl;\\\\csgenericrgb\\\\c0\\\\c0\\\\c0\\\\c100000;\\\\csgenericrgb\\\\c100000\\\\c100000\\\\c100000\\\\c100000;\\\\csgenericrgb\\\\c100000\\\\c100000\\\\c100000\\\\c0;}{\\\\*\\\\listtable}{\\\\*\\\\listoverridetable}\\\\uc1\\\\paperw12240\\\\margl0\\\\margr0\\\\margt0\\\\margb0\\\\pard\\\\li0\\\\fi0\\\\ri0\\\\ql\\\\sb0\\\\sa0\\\\sl240\\\\slmult1\\\\slleading0\\\\f0\\\\b0\\\\i0\\\\ul0\\\\strike0\\\\fs100\\\\expnd0\\\\expndtw0\\\\cf1\\\\strokewidth0\\\\strokec2\\\\nosupersub\\\\ulc0\\\\highlight3\\\\cb3}"
            attributes {
                font {
                name: "ArialMT"
                size: 50
                family: "Arial"
                face: "Regular"
                }
                text_solid_fill {
                alpha: 1
                }
                paragraph_style {
                line_height_multiple: 1
                text_list {
                }
                }
                stroke_color {
                red: 1
                green: 1
                blue: 1
                alpha: 1
                }
            }
            }
            chord_chart {
            }
        }
        }
    }
    isEnabled: true
}
ccli {
    song_title: "{{ song_name }}"
}
timeline {
    duration: 300
}"""
