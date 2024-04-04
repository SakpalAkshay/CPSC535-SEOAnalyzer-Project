from suffix_trees import STree

def count_pattern_occurrences(text, pattern):
    # Create a suffix tree from the text
    st = STree.STree(text)

    # Search for the pattern in the suffix tree
    occurrences = st.find_all(pattern)

    return len(occurrences)

