import maha.parsers.rules.numeral.expression as numeral_expression
from maha.expressions import EXPRESSION_SPACE, EXPRESSION_SPACE_OR_NONE
from maha.parsers.expressions import ALL_ALEF, SUM_SUFFIX, TWO_SUFFIX
from maha.parsers.templates import ValueExpression
from maha.rexy import Expression, non_capturing_group

TEN_SUFFIX = Expression(f"{EXPRESSION_SPACE_OR_NONE}[تط]?[اع]?شر?[ةه]?")
TEN_SUFFIX_SIMPLE = Expression(f"{EXPRESSION_SPACE}عشر[ةه]?")
TEH_OPTIONAL_SUFFIX = Expression("[ةه]?")
ALEF_LAM = Expression(non_capturing_group("ال"))
ALEF_LAM_OPTIONAL = Expression(ALEF_LAM + "?")


PREFIX_OF_ONE = Expression("واحد")
PREFIX_OF_TWO = Expression(non_capturing_group("[تث]ان[يى]", "[إا]?[ثت]نت؟[يى]"))
PREFIX_OF_THREE = Expression("[تث]ال[ثت]")
PREFIX_OF_FOUR = Expression("رابع")
PREFIX_OF_FIVE = Expression("خامس")
PREFIX_OF_SIX = Expression("سادس")
PREFIX_OF_SEVEN = Expression("سابع")
PREFIX_OF_EIGHT = Expression("[تث]امن")
PREFIX_OF_NINE = Expression("تاسع")
PREFIX_OF_TEN = Expression("عاشر")


EXPRESSION_OF_ONE = ValueExpression(1, ALEF_LAM + PREFIX_OF_ONE + TEH_OPTIONAL_SUFFIX)
EXPRESSION_OF_TWO = ValueExpression(2, ALEF_LAM + PREFIX_OF_TWO + TEH_OPTIONAL_SUFFIX)
EXPRESSION_OF_THREE = ValueExpression(
    3, ALEF_LAM + PREFIX_OF_THREE + TEH_OPTIONAL_SUFFIX
)
EXPRESSION_OF_FOUR = ValueExpression(4, ALEF_LAM + PREFIX_OF_FOUR + TEH_OPTIONAL_SUFFIX)
EXPRESSION_OF_FIVE = ValueExpression(5, ALEF_LAM + PREFIX_OF_FIVE + TEH_OPTIONAL_SUFFIX)
EXPRESSION_OF_SIX = ValueExpression(6, ALEF_LAM + PREFIX_OF_SIX + TEH_OPTIONAL_SUFFIX)
EXPRESSION_OF_SEVEN = ValueExpression(
    7, ALEF_LAM + PREFIX_OF_SEVEN + TEH_OPTIONAL_SUFFIX
)
EXPRESSION_OF_EIGHT = ValueExpression(
    8, ALEF_LAM + PREFIX_OF_EIGHT + TEH_OPTIONAL_SUFFIX
)
EXPRESSION_OF_NINE = ValueExpression(9, ALEF_LAM + PREFIX_OF_NINE + TEH_OPTIONAL_SUFFIX)

EXPRESSION_OF_ONE_ONLY = ValueExpression(1, ALEF_LAM_OPTIONAL + "[أا]ول[ىي]?")
EXPRESSION_OF_TWO_ONLY = ValueExpression(
    2, ALEF_LAM_OPTIONAL + "[تث]ان[يى]" + TEH_OPTIONAL_SUFFIX
)
EXPRESSION_OF_THREE_ONLY = ValueExpression(
    3, ALEF_LAM_OPTIONAL + PREFIX_OF_THREE + TEH_OPTIONAL_SUFFIX
)
EXPRESSION_OF_FOUR_ONLY = ValueExpression(
    4, ALEF_LAM_OPTIONAL + PREFIX_OF_FOUR + TEH_OPTIONAL_SUFFIX
)
EXPRESSION_OF_FIVE_ONLY = ValueExpression(
    5, ALEF_LAM_OPTIONAL + PREFIX_OF_FIVE + TEH_OPTIONAL_SUFFIX
)
EXPRESSION_OF_SIX_ONLY = ValueExpression(
    6, ALEF_LAM_OPTIONAL + PREFIX_OF_SIX + TEH_OPTIONAL_SUFFIX
)
EXPRESSION_OF_SEVEN_ONLY = ValueExpression(
    7, ALEF_LAM_OPTIONAL + PREFIX_OF_SEVEN + TEH_OPTIONAL_SUFFIX
)
EXPRESSION_OF_EIGHT_ONLY = ValueExpression(
    8, ALEF_LAM_OPTIONAL + PREFIX_OF_EIGHT + TEH_OPTIONAL_SUFFIX
)
EXPRESSION_OF_NINE_ONLY = ValueExpression(
    9, ALEF_LAM_OPTIONAL + PREFIX_OF_NINE + TEH_OPTIONAL_SUFFIX
)
EXPRESSION_OF_TEN = ValueExpression(
    10, ALEF_LAM_OPTIONAL + PREFIX_OF_TEN + TEH_OPTIONAL_SUFFIX
)
EXPRESSION_OF_ELEVEN = ValueExpression(
    11,
    non_capturing_group(
        ALEF_LAM + f"{ALL_ALEF}?حد[اى]?" + TEN_SUFFIX,
        ALEF_LAM_OPTIONAL + "حاد[يى]" + TEN_SUFFIX_SIMPLE,
    ),
)
EXPRESSION_OF_TWELVE = ValueExpression(
    12,
    non_capturing_group(
        ALEF_LAM
        + non_capturing_group(
            f"{ALL_ALEF}[طت]نا?" + TEN_SUFFIX,
            f"{ALL_ALEF}[ثت]نت?[اىي]ن?" + TEN_SUFFIX,
        ),
        ALEF_LAM_OPTIONAL + PREFIX_OF_TWO + TEN_SUFFIX_SIMPLE,
    ),
)
EXPRESSION_OF_THIRTEEN = ValueExpression(
    13, EXPRESSION_OF_THREE_ONLY + TEN_SUFFIX_SIMPLE
)
EXPRESSION_OF_FOURTEEN = ValueExpression(
    14, EXPRESSION_OF_FOUR_ONLY + TEN_SUFFIX_SIMPLE
)
EXPRESSION_OF_FIFTEEN = ValueExpression(15, EXPRESSION_OF_FIVE_ONLY + TEN_SUFFIX_SIMPLE)
EXPRESSION_OF_SIXTEEN = ValueExpression(16, EXPRESSION_OF_SIX_ONLY + TEN_SUFFIX_SIMPLE)
EXPRESSION_OF_SEVENTEEN = ValueExpression(
    17, EXPRESSION_OF_SEVEN_ONLY + TEN_SUFFIX_SIMPLE
)
EXPRESSION_OF_EIGHTEEN = ValueExpression(
    18, EXPRESSION_OF_EIGHT_ONLY + TEN_SUFFIX_SIMPLE
)
EXPRESSION_OF_NINETEEN = ValueExpression(
    19, EXPRESSION_OF_NINE_ONLY + TEN_SUFFIX_SIMPLE
)
EXPRESSION_OF_TWENTY = ValueExpression(20, ALEF_LAM + "عشر" + SUM_SUFFIX)
EXPRESSION_OF_THIRTY = ValueExpression(
    30, ALEF_LAM + numeral_expression.PREFIX_OF_THREE + SUM_SUFFIX
)
EXPRESSION_OF_FORTY = ValueExpression(
    40, ALEF_LAM + numeral_expression.PREFIX_OF_FOUR + SUM_SUFFIX
)
EXPRESSION_OF_FIFTY = ValueExpression(
    50, ALEF_LAM + numeral_expression.PREFIX_OF_FIVE + SUM_SUFFIX
)
EXPRESSION_OF_SIXTY = ValueExpression(
    60, ALEF_LAM + numeral_expression.PREFIX_OF_SIX + SUM_SUFFIX
)
EXPRESSION_OF_SEVENTY = ValueExpression(
    70, ALEF_LAM + numeral_expression.PREFIX_OF_SEVEN + SUM_SUFFIX
)
EXPRESSION_OF_EIGHTY = ValueExpression(
    80, ALEF_LAM + numeral_expression.PREFIX_OF_EIGHT + SUM_SUFFIX
)
EXPRESSION_OF_NINETY = ValueExpression(
    90, ALEF_LAM + numeral_expression.PREFIX_OF_NINE + SUM_SUFFIX
)


EXPRESSION_OF_HUNDRED = ValueExpression(100, ALEF_LAM + "ما?[يئ][ةه]")
EXPRESSION_OF_TWO_HUNDREDS = ValueExpression(200, ALEF_LAM + "م[يئ]ت" + TWO_SUFFIX)
EXPRESSION_OF_THREE_HUNDREDS = ValueExpression(
    300,
    ALEF_LAM
    + numeral_expression.EXPRESSION_OF_THREE
    + EXPRESSION_SPACE_OR_NONE
    + numeral_expression.EXPRESSION_OF_HUNDRED,
)
EXPRESSION_OF_FOUR_HUNDREDS = ValueExpression(
    400,
    ALEF_LAM
    + numeral_expression.EXPRESSION_OF_FOUR
    + EXPRESSION_SPACE_OR_NONE
    + numeral_expression.EXPRESSION_OF_HUNDRED,
)
EXPRESSION_OF_FIVE_HUNDREDS = ValueExpression(
    500,
    ALEF_LAM
    + numeral_expression.EXPRESSION_OF_FIVE
    + EXPRESSION_SPACE_OR_NONE
    + numeral_expression.EXPRESSION_OF_HUNDRED,
)
EXPRESSION_OF_SIX_HUNDREDS = ValueExpression(
    600,
    ALEF_LAM
    + numeral_expression.EXPRESSION_OF_SIX
    + EXPRESSION_SPACE_OR_NONE
    + numeral_expression.EXPRESSION_OF_HUNDRED,
)
EXPRESSION_OF_SEVEN_HUNDREDS = ValueExpression(
    700,
    ALEF_LAM
    + numeral_expression.EXPRESSION_OF_SEVEN
    + EXPRESSION_SPACE_OR_NONE
    + numeral_expression.EXPRESSION_OF_HUNDRED,
)
EXPRESSION_OF_EIGHT_HUNDREDS = ValueExpression(
    800,
    ALEF_LAM
    + numeral_expression.EXPRESSION_OF_EIGHT
    + EXPRESSION_SPACE_OR_NONE
    + numeral_expression.EXPRESSION_OF_HUNDRED,
)
EXPRESSION_OF_NINE_HUNDREDS = ValueExpression(
    900,
    ALEF_LAM
    + numeral_expression.EXPRESSION_OF_NINE
    + EXPRESSION_SPACE_OR_NONE
    + numeral_expression.EXPRESSION_OF_HUNDRED,
)
EXPRESSION_OF_HUNDREDS = ValueExpression(100, ALEF_LAM + "م[يئ]ات")

EXPRESSION_OF_THOUSAND = ValueExpression(1000, ALEF_LAM + "[أا]لف")
EXPRESSION_OF_TWO_THOUSANDS = ValueExpression(
    2000, ALEF_LAM + EXPRESSION_OF_THOUSAND + TWO_SUFFIX
)
EXPRESSION_OF_MILLION = ValueExpression(1000000, ALEF_LAM + "مليون")
EXPRESSION_OF_TWO_MILLIONS = ValueExpression(
    2000000, ALEF_LAM + EXPRESSION_OF_MILLION + TWO_SUFFIX
)
EXPRESSION_OF_BILLION = ValueExpression(
    1000000000, ALEF_LAM + non_capturing_group("بليون", "مليار")
)
EXPRESSION_OF_TWO_BILLIONS = ValueExpression(
    2000000000, ALEF_LAM + EXPRESSION_OF_BILLION + TWO_SUFFIX
)
EXPRESSION_OF_TRILLION = ValueExpression(1000000000000, "تري?ليون")
EXPRESSION_OF_TWO_TRILLIONS = ValueExpression(
    2000000000000, ALEF_LAM + EXPRESSION_OF_TRILLION + TEN_SUFFIX_SIMPLE
)
