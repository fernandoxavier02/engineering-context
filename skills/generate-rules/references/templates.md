# Rule Templates

Detailed templates for generating each engineering rule. Adapt ALL placeholders to the actual project.

## Rule 50: Architecture Contract Template

```markdown
# Contrato de Arquitetura (OBRIGATÓRIO)

## ⛔ NUNCA (violação = implementação inválida)

- `[core/ layer]` NUNCA importa de `[outer layers]`
- `[Layer A]` NUNCA importa de `[Layer B]`
- Código de venue/adapter NUNCA fora de `[adapter directory]`
- Lógica de [domain concern] NUNCA fora de `[domain directory]`
- NUNCA `print()` — usar `[logging lib]`
- NUNCA secrets hardcoded — usar `[config lib]` + `.env`
- NUNCA atalho: `[bypass pattern]`

## Camadas (dependências apontam PARA DENTRO)

[layer diagram — ASCII art showing dependency direction]

## Regras de Dependência

| Camada | Pode importar de | PROIBIDO importar de |
|--------|-----------------|---------------------|
| `[core]` | Libs externas apenas | `[list forbidden]` |
| `[service]` | `[core]` | `[list forbidden]` |
| `[adapter]` | `[service], [core]` | `[list forbidden]` |
| `[entry]` | All internal layers | Conter lógica de negócio |

## Fluxo Obrigatório

[mandatory flow pattern from architecture map]

## Quando CONSULTAR o Vault

- SE implementando [component] -> `vault:engineering/adr-[N]`
- SE criando [new module type] -> `vault:engineering/adr-[N]`
- SE em dúvida sobre camada -> `vault:engineering/layer-contract`
```

## Rule 51: Engineering Principles Template

```markdown
# Princípios de Engenharia (OBRIGATÓRIO)

## ⛔ NUNCA

- NUNCA criar abstração com menos de 3 implementações concretas
- NUNCA silenciar exceções com `[language-specific catch-all]`
- NUNCA implementar funcionalidade que não foi pedida na spec (YAGNI)
- NUNCA duplicar constante/lógica que já existe em outro lugar (DRY)

## SOLID — Neste Projeto

| Princípio | Significa aqui | ✅ Certo | ❌ Errado |
|-----------|---------------|----------|----------|
| **SRP** | [real module] SÓ [one job]. | [correct example from codebase] | [wrong example] |
| **OCP** | [extension pattern]. Zero mudança em [core]. | [correct example] | [wrong example] |
| **ISP** | [interface principle]. | [correct example] | [wrong example] |
| **DIP** | Depender de [abstractions]. | `param: AbstractType` | `param: ConcreteType` |

## DRY / YAGNI / KISS

- **DRY**: [concrete duplication example from codebase] -> Extrair para [single location]
- **YAGNI**: Não adicionar lógica "porque vai precisar um dia" -> Implementar SÓ o que a spec pede
- **KISS**: Função de 10 linhas > hierarquia de 5 classes

## Acoplamento

- Se módulo A precisa de detalhes internos de B -> acoplamento excessivo -> refatorar
- Se um teste precisa mockar mais de 3 coisas -> simplificar código

## Tratamento de Erros

| Tipo de erro | O que fazer | Exemplo |
|-------------|------------|---------|
| Domínio | `[language-specific exception]` | `[real example]` |
| Infra | `try/except` específico + log + retry | `[real example]` |
| Validação | Falha rápido, mensagem clara | `[real example]` |

## Regra de Ouro

Quando em dúvida, escolha a solução com **menos classes** e **menos imports**.

## Quando CONSULTAR o Vault

- SE criando novo módulo -> `vault:engineering/pattern-srp-examples`
- SE em dúvida entre herança vs composição -> `vault:engineering/pattern-composition-vs-inheritance`
```

## Rule 52: Testing Strategy Template

```markdown
# Estratégia de Testes (OBRIGATÓRIO)

## ⛔ NUNCA

- NUNCA marcar task como completa sem teste passando
- NUNCA silenciar teste falhando (skip/xfail sem justificativa)
- NUNCA escrever teste que valida implementação em vez de comportamento
- NUNCA continuar implementando se a suite de regressão falhou

## Tipo de Teste por Camada

| Camada | Tipo | O que testa | Onde fica |
|--------|------|------------|-----------|
| `[core/domain]` | Unitário + Comportamento | [what] | `[test dir pattern]` |
| `[adapter/infra]` | Integração | [what] | `[test dir pattern]` |
| `[entry/scripts]` | Smoke | [what] | `[test dir pattern]` |

## Tipo de Teste por Situação

| Situação | Teste OBRIGATÓRIO | Exemplo |
|----------|-------------------|---------|
| Bug fix | **Regressão** que reproduz o bug | `test_[bug_description]` |
| Nova feature | **Comportamento** do contrato público | `test_[feature_behavior]` |
| Refactor | Rodar suite EXISTENTE antes e depois | `[test command]` |
| Mudança de schema | **Contrato** atualizado PRIMEIRO | `test_[contract]` |

## Regressão (A MAIS IMPORTANTE)

1. Após QUALQUER alteração: `[test command]` na suite completa
2. Teste que passava e falha -> **PARAR TUDO** -> corrigir antes de continuar
3. Testes TDD promovidos a regressão ao final de cada checkpoint

## Quando CONSULTAR o Vault

- SE escrevendo teste de integração -> `vault:engineering/pattern-integration-testing`
- SE em dúvida sobre tipo de teste -> `vault:engineering/testing-strategy-examples`
```

## Rule 53: Anti-Patterns Template

```markdown
# Anti-Patterns (OBRIGATÓRIO)

## ⛔ NUNCA (erros já cometidos neste projeto)

| # | Anti-pattern | O que aconteceu | Como evitar |
|---|-------------|-----------------|-------------|
| 1 | [name] | [what happened] | [how to avoid] |
| ... | ... | ... | ... |

## Regra de Evolução

Quando corrigir um bug que não tinha teste:
1. **DEVE** criar teste de regressão que reproduz o bug
2. **DEVE** adicionar entrada nesta tabela
3. **DEVE** adicionar card no vault: `vault:engineering/anti-[name].md`

## Quando CONSULTAR o Vault

- SE corrigindo bug -> verificar se é anti-pattern recorrente em `vault:engineering/anti-*`
```

## Vault Card Templates

### ADR Template

```markdown
# ADR-[N]: [Decision Title]

**Status:** Accepted
**Date:** [YYYY-MM-DD]

## Context
[Why this decision was needed]

## Decision
[What was decided]

## Alternatives Considered
1. [Alternative 1] — rejected because [reason]
2. [Alternative 2] — rejected because [reason]

## Consequences
- Positive: [benefits]
- Negative: [trade-offs]
- Neutral: [side effects]
```

### Layer Contract Template

```markdown
# Layer Contract

## Import Rules

### [Layer Name]
**CAN import:**
```[language]
import [allowed_import]
```

**CANNOT import:**
```[language]
import [forbidden_import]  // VIOLATION
```
```
