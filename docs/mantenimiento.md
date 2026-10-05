# Mantener el perfil

## Regenerar gráficos

`python3 scripts/generate-assets.py` requiere Pillow y una fuente TrueType/OTF local. El script genera los SVG del README y una portada PNG para LinkedIn. No usa servicios externos, estadísticas remotas ni porcentajes subjetivos de dominio.

## Revisión de proyectos — 2026-10-05

| Repositorio | Evidencia revisada | Siguiente mejora |
| --- | --- | --- |
| UTECdiagram | README identifica hackathon; package.json confirma React/TypeScript | Documentar problema, aporte individual y capturas |
| django-quality-demo | README documenta instalación, pruebas y propósito didáctico | Ejecutar antes de afirmar cobertura o resultados |
| frontend | Descripción pública identifica Cine, S3 y microservicios | Revisar código, flujo completo y documentación de despliegue |
| tutor-ai-final-v-2-4-5 | package.json; README de instalación genérico | Revisar funcionalidad y versiones antes de destacar |
| Proyecto_final_cloud | package.json; README solo «grupo 6» | Documentar alcance y diferenciar frontend de infraestructura |

La selección no certifica ejecución, seguridad o calidad de los proyectos. No se renombraron, archivaron ni eliminaron repositorios. Para reorganizarlos, comparar versiones y dependencias antes de elegir repositorios canónicos.

## LinkedIn

Propuesta de titular breve: «CTO & Co-Founder at Psicogni | Software Engineer | Full-stack SaaS & Digital Health | Computer Science @ UTEC».

La sección Acerca de actual ya es coherente. Agregar tres elementos en Destacados: GitHub, un proyecto con demo verificable y un caso de producto autorizado para divulgación. La portada está en assets/linkedin-cover.png; aplicar desde Añadir imagen de fondo y revisar el recorte con la foto de perfil.

## Procedencia

Experiencia y stack: perfil de LinkedIn proporcionado por el usuario y leído con su sesión iniciada. Proyectos: API pública de GitHub. Inspiración estructural: https://github.com/macu-dev/macu-dev. No se copió código ni imágenes: GitHub no identificó una licencia del repositorio de referencia. Los gráficos de este perfil son originales.

Entrada anterior: sin bio ni README de perfil; repositorio granitespinoza/granitespinoza no existía. No se publican métricas de experiencia, cobertura o impacto sin verificar.

## Resultado de publicación

README público publicado en granitespinoza/granitespinoza y comprobado visualmente en el perfil. Portada original aplicada a LinkedIn; margen de texto aumentado tras revisar la vista móvil. Descripciones de UTECdiagram y django-quality-demo actualizadas. La biografía lateral y el enlace de GitHub siguen pendientes: la conexión CLI no tiene scope user (PATCH /user rechazado). No se amplió el permiso. La selección de repositorios fijados y Destacados en LinkedIn queda pendiente.

Preferencia del usuario (2026-10-05): portada de LinkedIn más modesta y profesional. Se sustituyó la portada tipográfica por un fondo original azul/gris sin texto ni diagramas, assets/linkedin-cover-modest.png. Es una imagen generada; el generador Python conserva la variante anterior y no reproduce esta imagen. El banner de GitHub no cambia.

## Segunda mejora — proyectos y enlaces

- README de UTECdiagram ampliado con flujo, estructura, endpoints y dos desajustes de integración identificados por lectura del código.
- README del tutor educativo sustituido por documentación de prototipo con datos simulados; no se atribuye una integración real de IA o Google Classroom.
- README de django-quality-demo conserva la guía original y añade un resumen, referencias de observabilidad y una aclaración sobre los placeholders del workflow.
- El perfil reemplaza Cine Frontend por el tutor educativo: frontend solo contiene configuración y no el código de la aplicación.
- Los tres README remotos se compararon byte a byte con los documentos preparados; coincidieron. No se afirma build, lint o cobertura ejecutados.
- No renombrar, archivar ni eliminar versiones antes de contrastar su contenido y dependencias. Próximo orden: escoger versión canónica del tutor y reunir evidencia visual verificable de los dos frontends.
- Preferencia persistente del usuario: no activar «Notificar a tu red» ni crear publicaciones de actualización.
- Destacados de LinkedIn: falló la carga de vista previa tanto del perfil GitHub como del repositorio de perfil; Guardar permaneció deshabilitado. No se creó la tarjeta.
