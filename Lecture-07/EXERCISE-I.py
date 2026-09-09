survey_results = [
    ["Python", "JavaScript", "C++"],
    ["Python", "JavaScript", "C#"],
    ["Python", "Java"],
    ["Python", "C++", "JavaScript"],
    ["Python", "JavaScript", "C++", "Java"],
]

choices_sets = [set(p) for p in survey_results]

# 1. Languages chosen by all participants
common_languages = set.intersection(*choices_sets)
print("1. Languages chosen by all participants:", common_languages)

# 2. Languages chosen by only one participant
language_counts = {}
for participant_choices in choices_sets:
    for language in participant_choices:
        language_counts[language] = language_counts.get(language, 0) + 1

only_one_participant = {language for language, count in language_counts.items() if count == 1}
print("2. Languages only chosen by one participant:", only_one_participant)

# 3. Number of unique languages
unique_languages = set().union(*choices_sets)
print("3. Number of unique languages:", len(unique_languages))

# 4. Languages chosen by exactly two participants
exactly_two_participants = {language for language, count in language_counts.items() if count == 2}
print("4. Languages chosen by exactly two participants:", exactly_two_participants)

# 5. Participants with the same set of languages
participant_groups = {}
for index, participant_choices in enumerate(choices_sets, start=1):
    participant_groups.setdefault(frozenset(participant_choices), []).append(index)

same_language_participants = [indices for indices in participant_groups.values() if len(indices) > 1]
print("5. Participants with the same set of languages:", same_language_participants[0] if same_language_participants else [])
