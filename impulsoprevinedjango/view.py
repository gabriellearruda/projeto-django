# -*- encoding:utf-8 -*-
# Usado para encontrar urls
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView
from .formulario import DadosBanco
import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from pandas.io import sql

def readQuery(query):
    engine = create_engine(
      'postgresql://{}:{}@{}:{}/{}?'.format("postgres",
                        "root",
                        "localhost",
                        "5432",
                        "postgres"), connect_args={"options": "-c statement_timeout=100000000"}
    )
    conexao = engine.connect()
    resultados = sql.read_sql(query, conexao)
    return resultados


class Inicio(TemplateView):
    template_name = 'inicio.html'

class Impulso(TemplateView):
    template_name = 'impulso.html'

class Indicadores(TemplateView):
    template_name = 'indicadores.html'

class Previne(TemplateView):
    template_name = 'previne.html'

class DadosAdm(TemplateView): # new
    form_class = DadosBanco
    template_name = 'dados.html'

    def get_context_data(self, **kwargs):
        context = super(DadosAdm, self).get_context_data(**kwargs)
        context['form'] = DadosBanco()
        context['action_link'] = reverse("graficos")
        return context

class Graficos(TemplateView):
    template_name = 'graficos.html'

    def get_context_data(self, **kwargs):
        context = super(Graficos, self).get_context_data(**kwargs)
        query = """
        SELECT municipio_nome, estado_id, periodo_codigo, 
        indicadores_parametros_nome, indicadores_parametros_meta, indicadores_parametros_ordem,
        indicadores_resultados_porcentagem, indicadores_nota_calculado, indicadores_niveis_nivel
        FROM prod.visualizacao_indicadores;
        """
        query_piraju = """
        SELECT 
            * 
            FROM
            (
            SELECT DISTINCT ON (nu_cns, nu_cpf_cidadao) 
                CASE WHEN nu_cns IS NULL THEN '0'
                    ELSE TRIM(FROM nu_cns) END
                    nu_cns,
                CASE WHEN nu_cpf_cidadao IS NULL THEN '0'
                    ELSE TRIM(FROM nu_cpf_cidadao) END
                    nu_cpf_cidadao,
                CASE WHEN co_dim_cbo_1 = 1 THEN co_dim_cbo_2
                    ELSE co_dim_cbo_1 END
                    co_dim_cbo,
                CASE WHEN co_dim_unidade_saude_1 = 1 THEN co_dim_unidade_saude_2
                    ELSE co_dim_unidade_saude_1 END
                    co_dim_unidade_saude,
                CASE WHEN co_dim_equipe_1 = 1 THEN co_dim_equipe_2
                    ELSE co_dim_equipe_1 END
                    co_dim_equipe,
                co_dim_tempo,
                dt_nascimento,
                co_dim_tempo_dum
            FROM
                tb_fat_atendimento_individual
            WHERE
                co_dim_tempo_dum >= ".$ndti." AND 
                co_dim_tempo_dum < ".$ndtf."
                AND (
                    ds_filtro_ciaps LIKE ANY (
                        array[
                            '%|W03|%',
                            '%|W05|%',
                            '%|W29|%',
                            '%|W71|%',
                            '%|W78|%',
                            '%|W79|%',
                            '%|W80|%',
                            '%|W81|%',
                            '%|W84|%',
                            '%|W85|%',
                            --'%|W72|%',
                            --'%|W73|%',
                            --'%|W75|%',
                            --'%|W76|%',
                            '%|ABP001|%'
                        ]
                    ) OR
                    ds_filtro_cids LIKE ANY (
                        array[
                            '%|O11|%',
                            '%|O120|%',
                            '%|O121|%',
                            '%|O122|%',
                            '%|O13|%',
                            '%|O140|%',
                            '%|O141|%',
                            '%|O149|%',
                            '%|O150|%',
                            '%|O151|%',
                            '%|O159|%',
                            '%|O16|%',
                            '%|O200|%',
                            '%|O208|%',
                            '%|O209|%',
                            '%|O210|%',
                            '%|O211|%',
                            '%|O212|%',
                            '%|O218|%',
                            '%|O219|%',
                            '%|O220|%',
                            '%|O221|%',
                            '%|O222|%',
                            '%|O223|%',
                            '%|O224|%',
                            '%|O225|%',
                            '%|O228|%',
                            '%|O229|%',
                            '%|O230|%',
                            '%|O231|%',
                            '%|O232|%',
                            '%|O233|%',
                            '%|O234|%',
                            '%|O235|%',
                            '%|O239|%',
                            '%|O299|%',
                            '%|O300|%',
                            '%|O301|%',
                            '%|O302|%',
                            '%|O308|%',
                            '%|O309|%',
                            '%|O311|%',
                            '%|O312|%',
                            '%|O318|%',
                            '%|O320|%',
                            '%|O321|%',
                            '%|O322|%',
                            '%|O323|%',
                            '%|O324|%',
                            '%|O325|%',
                            '%|O326|%',
                            '%|O328|%',
                            '%|O329|%',
                            '%|O330|%',
                            '%|O331|%',
                            '%|O332|%',
                            '%|O333|%',
                            '%|O334|%',
                            '%|O335|%',
                            '%|O336|%',
                            '%|O337|%',
                            '%|O338|%',
                            '%|O752|%',
                            '%|O753|%',
                            '%|O990|%',
                            '%|O991|%',
                            '%|O992|%',
                            '%|O993|%',
                            '%|O994|%',
                            '%|O240|%',
                            '%|O241|%',
                            '%|O242|%',
                            '%|O243|%',
                            '%|O244|%',
                            '%|O249|%',
                            '%|O25|%',
                            '%|O260|%',
                            '%|O261|%',
                            '%|O263|%',
                            '%|O264|%',
                            '%|O265|%',
                            '%|O268|%',
                            '%|O269|%',
                            '%|O280|%',
                            '%|O281|%',
                            '%|O282|%',
                            '%|O283|%',
                            '%|O284|%',
                            '%|O285|%',
                            '%|O288|%',
                            '%|O289|%',
                            '%|O290|%',
                            '%|O291|%',
                            '%|O292|%',
                            '%|O293|%',
                            '%|O294|%',
                            '%|O295|%',
                            '%|O296|%',
                            '%|O298|%',
                            '%|O009|%',
                            '%|O339|%',
                            '%|O340|%',
                            '%|O341|%',
                            '%|O342|%',
                            '%|O343|%',
                            '%|O344|%',
                            '%|O345|%',
                            '%|O346|%',
                            '%|O347|%',
                            '%|O348|%',
                            '%|O349|%',
                            '%|O350|%',
                            '%|O351|%',
                            '%|O352|%',
                            '%|O353|%',
                            '%|O354|%',
                            '%|O355|%',
                            '%|O356|%',
                            '%|O357|%',
                            '%|O358|%',
                            '%|O359|%',
                            '%|O360|%',
                            '%|O361|%',
                            '%|O362|%',
                            '%|O363|%',
                            '%|O365|%',
                            '%|O366|%',
                            '%|O367|%',
                            '%|O368|%',
                            '%|O369|%',
                            '%|O40|%',
                            '%|O410|%',
                            '%|O411|%',
                            '%|O418|%',
                            '%|O419|%',
                            '%|O430|%',
                            '%|O431|%',
                            '%|O438|%',
                            '%|O439|%',
                            '%|O440|%',
                            '%|O441|%',
                            '%|O460|%',
                            '%|O468|%',
                            '%|O469|%',
                            '%|O470|%',
                            '%|O471|%',
                            '%|O479|%',
                            '%|O48|%',
                            '%|O995|%',
                            '%|O996|%',
                            '%|O997|%',
                            '%|Z640|%',
                            '%|O00|%',
                            '%|O10|%',
                            '%|O12|%',
                            '%|O14|%',
                            '%|O15|%',
                            '%|O20|%',
                            '%|O21|%',
                            '%|O22|%',
                            '%|O23|%',
                            '%|O24|%',
                            '%|O26|%',
                            '%|O28|%',
                            '%|O29|%',
                            '%|O30|%',
                            '%|O31|%',
                            '%|O32|%',
                            '%|O33|%',
                            '%|O34|%',
                            '%|O35|%',
                            '%|O36|%',
                            '%|O41|%',
                            '%|O43|%',
                            '%|O44|%',
                            '%|O46|%',
                            '%|O47|%',
                            '%|O98|%',
                            '%|Z34|%',
                            '%|Z35|%',
                            '%|Z36|%',
                            '%|Z321|%',
                            '%|Z33|%',
                            '%|Z340|%',
                            '%|Z340|%',
                            '%|Z348|%',
                            '%|Z349|%',
                            '%|Z350|%',
                            '%|Z351|%',
                            '%|Z352|%',
                            '%|Z353|%',
                            '%|Z354|%',
                            '%|Z357|%',
                            '%|Z358|%',
                            --'%|Z356|%',
                            '%|Z359|%'
                        ]
                    )
                )
            ORDER BY nu_cns, nu_cpf_cidadao".$cdum."
            ) AS t1
            ORDER BY co_dim_tempo_dum
        """
        df = readQuery(query)
        context['dados'] = json.loads(df.to_json(orient='records'))
        return context