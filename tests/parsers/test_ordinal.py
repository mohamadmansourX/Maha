import random
from itertools import chain
from typing import List

import pytest

from maha.parsers.functions import parse_dimension
from maha.parsers.rules.numeral import *
from maha.parsers.templates import Dimension, DimensionType

random.seed(0)


def assert_expression_output(output: List[Dimension], expected):
    assert len(output) == 1
    assert isinstance(output[0], Dimension)
    dim = output[0]

    assert dim.dimension_type == DimensionType.ORDINAL
    assert isinstance(dim.value, (float, int))
    assert pytest.approx(dim.value, 0.0001) == expected


def get_value_positions(*text: str):
    positions = [
        ("${}."),
        ("@{}"),
        ("!{}."),
        (".{} "),
        (",{}"),
        ("({},"),
        ("{},"),
        ("&{}"),
        ("{}"),
    ]
    for t in text:
        yield random.choice(positions).format(t)


def get_value(exprected: int, values: List[str]):
    for v in get_value_positions(*values):
        yield v, exprected


@pytest.mark.parametrize(
    "input, expected",
    chain(
        get_value(1, ["أول", "الاولى", "الأول", "اول"]),
        get_value(2, ["الثاني", "التاني", "الثانية", "التانيه", "تاني", "ثاني"]),
        get_value(3, ["التالت", "الثالثة", "ثالث"]),
        get_value(4, ["الرابع", "الرابعه", "رابع"]),
        get_value(5, ["الخامس", "خامس", "الخامسه", "خامسة"]),
        get_value(6, ["السادس", "سادس", "سادسة"]),
        get_value(7, ["السابع", "سابع", "السابعه"]),
        get_value(8, ["الثامن", "التامن", "التامنة", "ثامن", "تامن"]),
        get_value(9, ["التاسع", "التاسعه", "تاسعة", "تاسع"]),
    ),
)
def test_ones(input, expected):
    assert_expression_output(parse_dimension(input, ordinal=True), expected)


@pytest.mark.parametrize(
    "input, expected",
    chain(
        get_value(10, ["العاشر", "عاشر", "العاشرة"]),
        get_value(
            11, ["حادي عشر", "الاحدعشر", "الحادي عشرة", "الأحد عشر", "الإحدى عشره"]
        ),
        get_value(
            12, ["الثاني عشر", "التانى عشره", "الإثنتي عشر", "الإثني عشر", "ثاني عشرة"]
        ),
        get_value(
            13,
            ["الثالث عشرة", "الثالثة عشرة", "التالته عشر", "الثالث عشره", "ثالث عشر"],
        ),
        get_value(
            14,
            ["الرابع عشر", "الرابعة عشر", "رابع عشر", "الرابعه عشره", "رابع عشرة"],
        ),
        get_value(15, ["الخامس عشر", "خامس عشر", "الخامسة عشرة", "الخامس عشره"]),
        get_value(16, ["السادس عشر", "السادسة عشر", "سادسه عشره"]),
        get_value(17, ["السابع عشر", "السابعة عشره", "سابع عشر", "السابعه عشرة"]),
        get_value(18, ["التامن عشر", "ثامن عشر", "الثامنة عشر", "الثامنه عشره"]),
        get_value(19, ["التاسع  عشر", "تاسع عشرة", "التاسعة عشره"]),
    ),
)
def test_tens(input, expected):
    assert_expression_output(parse_dimension(input, ordinal=True), expected)


@pytest.mark.parametrize(
    "input, expected",
    chain(
        get_value(10, ["العاشر", "العاشرة", "العاشره"]),
        get_value(20, ["العشرون", "العشرين"]),
        get_value(30, ["الثلاثين", "الثلاثون", "التلاتين"]),
        get_value(40, ["الأربعين", "الأربعون", "الاربعين"]),
        get_value(50, ["الخمسين", "الخمسون"]),
        get_value(60, ["الستين", "الستون"]),
        get_value(70, ["السبعين", "السبعون"]),
        get_value(80, ["الثمانين", "الثمانون", "التمنين", "التمانون"]),
        get_value(90, ["التسعين", "التسعون"]),
    ),
)
def test_perfect_tens(input, expected):
    assert_expression_output(parse_dimension(input, ordinal=True), expected)


@pytest.mark.parametrize(
    "input, expected",
    chain(
        get_value(21, ["الواحد والعشرين", "الواحد والعشرون", "الواحدة والعشرون"]),
        get_value(32, ["الثاني والثلاثين", "الثاني والتلاتين", "الثانية والثلاثون"]),
        get_value(43, ["الثالثة والأربعين", "الثالث والأربعون"]),
        get_value(44, ["الرابع والاربعون", "الرابع والاربعون"]),
        get_value(54, ["الرابع والخمسين", "الرابع والخمسون"]),
        get_value(65, ["الخامس والستين", "الخامس والستون"]),
        get_value(76, ["السادس والسبعين", "السادس والسبعون"]),
        get_value(87, ["السابع والتمانين", "السابع والتمانون"]),
        get_value(98, ["الثامن والتسعين", "التامن والتسعون"]),
        get_value(99, ["التاسع والتسعين"]),
        get_value(91, ["الواحد والتسعين"]),
        get_value(66, ["السادس والستين"]),
        get_value(26, ["السادس والعشرين"]),
        get_value(25, ["الخامس و العشرون"]),
        get_value(75, ["الخامس والسبعين"]),
        get_value(22, ["الثاني و العشرون"]),
        get_value(22, ["التانية و العشرون"]),
    ),
)
def test_combines_tens(input, expected):
    assert_expression_output(parse_dimension(input, ordinal=True), expected)


@pytest.mark.parametrize(
    "input, expected",
    chain(
        get_value(100, ["المية", "الميه", "المائة", "المائه", "المئة", "المئه"]),
        get_value(200, ["الميتين", "المئتين", "المئتان"]),
        get_value(
            300,
            ["الثلاثمية", "الثلاثة مائة", "التلاتمية", "الثلاثمئه"],
        ),
        get_value(
            400,
            ["الأربعمية", "الأربعة مائة", "الاربعمية", "الاربعمئه"],
        ),
        get_value(
            500,
            ["الخمسمية", "الخمسة مئة", "الخمس مائة", "الخمسميه", "الخمسه مئة"],
        ),
        get_value(
            600,
            ["الستمية", "الستة مئة", "الست مائة", "الستميه", "الستمائة"],
        ),
        get_value(
            700,
            ["السبعمية", "السبعة مئة", "السبع مائة", "السبعميه", "السبعمائة"],
        ),
        get_value(
            800,
            ["الثمنمية", "الثماني مئة", "الثمان مائة", "التمنميه", "الثمانمائة"],
        ),
        get_value(
            900,
            ["التسعمية", "التسعة مئة", "التسع مائة", "التسعميه", "التسعمائة"],
        ),
    ),
)
def test_perfect_hundreds(input, expected):
    assert_expression_output(parse_dimension(input, ordinal=True), expected)


@pytest.mark.parametrize(
    "input, expected",
    chain(
        get_value(191, ["المية والواحد والتسعين"]),
        get_value(124, ["المائة والرابع والعشرين"]),
        get_value(215, ["المئتين والخامس عشر"]),
        get_value(306, ["الثلاثمية والسادس"]),
        get_value(410, ["الاربعمية والعاشر"]),
        get_value(520, ["الخمس مائة والعشرين"]),
        get_value(606, ["الستمية والسادس"]),
        get_value(780, ["السبعة مائة والثمانون"]),
        get_value(877, ["الثمنمية والسابع والسبعين"]),
        get_value(999, ["التسع مية والتاسع والتسعين"]),
    ),
)
def test_hundreds(input, expected):
    assert_expression_output(parse_dimension(input, ordinal=True), expected)


@pytest.mark.parametrize(
    "input, expected",
    chain(
        get_value(1000, ["الألف"]),
        get_value(1000000, ["المليون"]),
        get_value(1000000000, ["البليون", "المليار"]),
        get_value(1000000000000, ["التريليون", "الترليون"]),
        get_value(1100, ["الألف والمئة"]),
        get_value(1216, ["الألف والمئتين والسادس عشر"]),
        get_value(1000300, ["المليون والثلاثمئة"]),
        get_value(1000018, ["المليون والثامن عشر"]),
        get_value(1000000020, ["البليون والعشرين", "المليار والعشرون"]),
    ),
)
def test_perfect_millions(input, expected):
    assert_expression_output(parse_dimension(input, ordinal=True), expected)


# TODO:
# This behaviour might be changed in the future.
@pytest.mark.parametrize(
    "expected, input",
    [
        (141, "الأول والأربعين والمئة"),
        (16, "الثاني والرابع عشر"),
        (1000101, "الواحد والمئة والمليون"),
        # Is this alright?
        (6, "الأول والثاني والثالث"),
    ],
)
def test_combinations(input, expected):
    assert_expression_output(parse_dimension(input, ordinal=True), expected)


@pytest.mark.parametrize(
    "input",
    [
        ("واحد"),
        ("عشرين"),
        ("عشرة"),
        ("مئة"),
        ("الفتياني"),
        ("المليونير"),
        ("ولسادس"),
        ("وواثنين"),
    ],
)
def test_negative_simple_values(input: str):
    output = parse_dimension(input, ordinal=True)
    assert output == []
