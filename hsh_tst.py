from typing import Dict, List


folders:Dict[str,List[str]]={
        "images": ['.png','.jpeg'],
        "videos":['mp4'],
        "documents":[".txt",".docx"],
        "audio":["mp3",".wav"],
        "other":[]
    }

file_extensions = [

    # Common Document & Text Extensions
    ".txt", ".pdf", ".docx", ".xlsx", ".pptx", ".odt", ".rtf", ".md", ".json", ".xml",

    # Common Image Extensions
    ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp", ".svg", ".ico",

    # Common Audio Extensions
    ".mp3", ".wav", ".flac", ".aac", ".ogg", ".wma", ".m4a",

    # Common Video Extensions
    ".mp4", ".avi", ".mov", ".wmv", ".flv", ".mkv", ".webm", ".mpeg",

    # Common Code & Script Extensions
    ".py", ".js", ".html", ".css", ".java", ".cpp", ".c", ".h", ".cs", ".php", ".rb", ".go", ".swift", ".ts", ".jsx", ".vue", ".sh", ".ps1",

    # Archive & Compressed Extensions
    ".zip", ".rar", ".7z", ".tar.gz", ".iso", ".dmg", ".gz", ".bz2",

    # Database Extensions
    ".db", ".sqlite", ".sql", ".mdb", ".accdb",

    # Executable & System Extensions
    ".exe", ".dll", ".sys", ".app", ".bat", ".com", ".bin",

    # Design & CAD Extensions
    ".psd", ".ai", ".indd", ".dwg", ".dxf", ".skp", ".blend", ".obj", ".fbx",

    # Font Extensions
    ".ttf", ".otf", ".woff", ".woff2",

    # Web-related Extensions (beyond common code)
    ".yml", ".yaml", ".toml", ".env", ".htaccess",

    # Less Common / Niche Extensions
    ".tex", ".csv", ".tsv", ".log", ".dat", ".bak", ".tmp", ".cfg", ".ini", ".key", ".pem", ".crt", ".cer", ".pfx",

    # New / Made-up / Funky Extensions (just for you!)
    ".xyz", ".foo", ".bar", ".qux", ".grok", ".blorp", ".wobble", ".fuzzle", ".skrrt", ".dank", ".meme", ".lol", ".flex", ".swag", ".yolo", ".yeet", ".boop", ".bloop", ".glitch", ".pixel", ".vapor", ".synth", ".cyber", ".flux", ".quantum", ".nebula", ".vortex", ".chronos", ".arcane", ".cosmic", ".fusion", ".zenith", ".abyss", ".echo", ".phantom", ".nova", ".blitz", ".nexus", ".prism", ".stardust", ".dream", ".ether", ".glimmer", ".hush", ".lumen", ".mirage", ".oblivion", ".pylon", ".reverie", ".scepter", ".twilight", ".umbra", ".velvet", ".whisper", ".xeno", ".yonder", ".zest", ".doodad", ".gizmo", ".widget", ".spline", ".noodle", ".flibble", ".squanch"
]

"""
print(folders.items())
print()
print()
print()

print(folders.keys())
print()
print()
print()

print(type(folders.items()))

print(type(folders.values()))

print()
print()
print()

print(folders.values())


file_ext = file_extensions[:25:5]

for i in file_ext:
    for j in foder


"""
for i in folders.values():
    #print(i)
    for j in i:
        if j == ".exe":
            print(j, i)
        else:
            print(True,i,j)

ll = folders.keys()


#print(next(ll))
 
#oo = folders.keys
#print(next(oo))

#k, l= 
#print(k,l)

print(list(folders.items()))