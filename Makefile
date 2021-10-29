PY=python3
VENVDIR=venv
WITH_VENV=source $(VENVDIR)/bin/activate &&

TWINE=$(WITH_VENV) 		twine
TESTER=$(WITH_VENV) 	pytest
TOX=$(WITH_VENV) 		tox
BLACK=$(WITH_VENV) 		black
BUILDER=$(WITH_VENV) 	python3 -m build


.PHONY: check-worktree

build: venv
	$(BUILDER)

venv:
	@if [[ -d "$(VENVDIR)" ]]; then \
		echo "venv already exists"; \
		exit 0; \
	fi; \
	$(PY) -m venv $(VENVDIR) && \
	$(WITH_VENV) \
	pip install --upgrade pip && \
	pip install -r requirements.txt

pre-commit: test
	$(FORMAT) src
	@echo "Ready to commit 🙂"

test: venv
	$(TESTER)

tox: venv
	$(TOX)

clean:
	find . | grep egg-info | xargs rm -rfd
	rm -fr dist

check-worktree:
	git diff --quiet --exit-code; \
	if [[ $$? -ne 0 ]]; then \
		echo "Fatal: working tree is not clean"; \
		exit 1; \
	fi

dist-production: clean check-worktree build tox
	$(TWINE) upload dist/*

dist-test: clean build tox
	$(TWINE) upload --repository testpypi dist/*

