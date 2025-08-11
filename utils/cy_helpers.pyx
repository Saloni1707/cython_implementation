import re

cpdef str sanitize_text(str s):
    cdef list blacklist = ["badword1", "badword2", "offensive"]
    s = ' '.join(s.strip().split())

    # Build the regex pattern string safely
    cdef str pattern_str = r'\\b(' + '|'.join([re.escape(word) for word in blacklist]) + r')\\b'

    pattern = re.compile(pattern_str, re.IGNORECASE)
    clean_text = pattern.sub("[redacted]", s)
    return clean_text
