test target:
    python3 -m unittest {{justfile_directory()}}/test/{{target}}

pwd target:
    @echo {{target}}

gen-test target:
    touch {{justfile_directory()}}/test/{{target}}

echo target:
    @echo {{target}}

commit message:
    git add * 
    git commit -m "Add {{message}}"

push:
    git push