#!/usr/bin/env python3
"""
Testa a estrutura da skill agrobr para garantir que todos
os arquivos necessários existem e estão no formato correto.
"""
import json
import os
from pathlib import Path


def test_skill_directory_structure():
    """Verifica se a estrutura de diretórios está completa."""
    skill_dir = Path(__file__).parent.parent

    required_files = [
        "SKILL.md",
        "README.md",
        "LICENSE",
        "CHANGELOG.md",
        "CONTRIBUTING.md",
        "pyproject.toml",
        ".gitignore",
        "evals/evals.json",
        ".github/workflows/validate.yml",
        ".github/ISSUE_TEMPLATE/bug_report.md",
        ".github/ISSUE_TEMPLATE/feature_request.md",
        ".github/PULL_REQUEST_TEMPLATE.md",
    ]

    missing = []
    for f in required_files:
        if not (skill_dir / f).exists():
            missing.append(f)

    assert not missing, f"Arquivos ausentes: {missing}"
    print(f"✓ Estrutura de diretórios OK ({len(required_files)} arquivos verificados)")


def test_skill_md_format():
    """Verifica se SKILL.md tem o formato YAML frontmatter correto."""
    skill_dir = Path(__file__).parent.parent
    skill_md = skill_dir / "SKILL.md"

    content = skill_md.read_text(encoding="utf-8")

    # Deve começar com frontmatter YAML
    assert content.startswith("---"), "SKILL.md deve começar com '---'"

    # Deve ter name e description no frontmatter
    frontmatter_end = content.find("---", 3)
    assert frontmatter_end > 0, "SKILL.md deve ter frontmatter YAML fechado"

    frontmatter = content[3:frontmatter_end]
    assert "name:" in frontmatter, "Frontmatter deve ter campo 'name'"
    assert "description:" in frontmatter, "Frontmatter deve ter campo 'description'"

    # Name deve ser "agrobr"
    for line in frontmatter.split("\n"):
        if line.strip().startswith("name:"):
            assert "agrobr" in line, "name deve ser 'agrobr'"
            break

    print("✓ SKILL.md formato YAML frontmatter OK")


def test_evals_json():
    """Verifica se evals.json é válido e tem a estrutura correta."""
    skill_dir = Path(__file__).parent.parent
    evals_file = skill_dir / "evals" / "evals.json"

    with open(evals_file, encoding="utf-8") as f:
        data = json.load(f)

    # Estrutura básica
    assert "skill_name" in data, "evals.json deve ter 'skill_name'"
    assert data["skill_name"] == "agrobr", "skill_name deve ser 'agrobr'"
    assert "evals" in data, "evals.json deve ter 'evals'"
    assert isinstance(data["evals"], list), "'evals' deve ser uma lista"
    assert len(data["evals"]) >= 3, "Deve haver pelo menos 3 evals"

    # Cada eval deve ter campos obrigatórios
    for eval_item in data["evals"]:
        assert "id" in eval_item, f"Eval {eval_item.get('name', '?')} sem 'id'"
        assert "name" in eval_item, f"Eval {eval_item.get('id', '?')} sem 'name'"
        assert "prompt" in eval_item, f"Eval {eval_item['name']} sem 'prompt'"
        assert "expected_output" in eval_item, f"Eval {eval_item['name']} sem 'expected_output'"
        assert "assertions" in eval_item, f"Eval {eval_item['name']} sem 'assertions'"
        assert isinstance(eval_item["assertions"], list), f"Eval {eval_item['name']}: assertions deve ser lista"
        assert len(eval_item["assertions"]) >= 3, f"Eval {eval_item['name']}: deve ter pelo menos 3 assertions"

        # Cada assertion deve ter campos obrigatórios
        for assertion in eval_item["assertions"]:
            assert "name" in assertion, f"Assertion sem 'name' no eval {eval_item['name']}"
            assert "description" in assertion, f"Assertion '{assertion['name']}' sem 'description'"
            assert "expectation" in assertion, f"Assertion '{assertion['name']}' sem 'expectation'"

    print(f"✓ evals.json válido: {len(data['evals'])} evals, {sum(len(e['assertions']) for e in data['evals'])} assertions")


def test_readme_has_content():
    """Verifica se README.md tem conteúdo substancial."""
    skill_dir = Path(__file__).parent.parent
    readme = skill_dir / "README.md"

    content = readme.read_text(encoding="utf-8")

    assert len(content) > 500, f"README.md muito curto ({len(content)} chars)"
    assert "# " in content, "README.md deve ter pelo menos um título"
    assert "agrobr" in content.lower(), "README.md deve mencionar 'agrobr'"
    assert "instalação" in content.lower() or "pip install" in content.lower(), "README.md deve ter instruções de instalação"

    print(f"✓ README.md OK ({len(content)} caracteres)")


def test_license():
    """Verifica se LICENSE existe e contém MIT."""
    skill_dir = Path(__file__).parent.parent
    license_file = skill_dir / "LICENSE"

    content = license_file.read_text(encoding="utf-8")

    assert "MIT License" in content, "LICENSE deve ser MIT"
    assert "Permission is hereby granted" in content, "LICENSE deve ter texto padrão MIT"

    print("✓ LICENSE (MIT) OK")


def test_github_workflow():
    """Verifica se o workflow de CI está configurado."""
    skill_dir = Path(__file__).parent.parent
    workflow = skill_dir / ".github" / "workflows" / "validate.yml"

    content = workflow.read_text(encoding="utf-8")

    assert "on:" in content, "Workflow deve ter trigger"
    assert "jobs:" in content, "Workflow deve ter jobs"
    assert "test_skill_structure.py" in content, "Workflow deve rodar os testes"

    print("✓ GitHub Actions workflow OK")


def main():
    print("=" * 60)
    print("VALIDAÇÃO DA SKILL agrobr")
    print("=" * 60)
    print()

    tests = [
        test_skill_directory_structure,
        test_skill_md_format,
        test_evals_json,
        test_readme_has_content,
        test_license,
        test_github_workflow,
    ]

    passed = 0
    failed = 0

    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as e:
            print(f"✗ {test.__name__}: {e}")
            failed += 1
        except Exception as e:
            print(f"✗ {test.__name__}: Erro inesperado: {e}")
            failed += 1

    print()
    print("=" * 60)
    print(f"Resultado: {passed} passaram, {failed} falharam de {len(tests)} testes")
    print("=" * 60)

    if failed > 0:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
