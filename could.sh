#!/usr/bin/env bash

cat <<'EOF'
TEPTHON
                                                  
                                                  
                                                  
Copyright (C) 2020-2024 by Zelzal-SC@Github, < https://github.com/Tepthonee >.
This file is part of < https://github.com/Tepthonee/ArTepStrings > project,
and is released under the "GNU v3.0 License Agreement".
Please see < https://github.com/Tepthonee/ArTepStrings/blob/main/LICENSE >
All rights reserved.
EOF

gunicorn app:app --daemon && python -m ArStringTep
