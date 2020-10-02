#
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
#
import math

import pandas as pd

from mlos.Spaces import CategoricalDimension, ContinuousDimension, Hypergrid, Point, SimpleHypergrid
from mlos.OptimizerEvaluationTools.ObjectiveFunctionBase import ObjectiveFunctionBase
from mlos.OptimizerEvaluationTools.SyntheticFunctions.PolynomialObjective import PolynomialObjective
from mlos.OptimizerEvaluationTools.SyntheticFunctions.PolynomialObjectiveWrapper import PolynomialObjectiveWrapper

class NestedPolynomialObjective(ObjectiveFunctionBase):
    """ Wraps the PolynomialObjective to provide the interface defined in the ObjectiveFunctionBase.

    """

    def __init__(self, objective_function_config: Point):
        assert objective_function_config.polynomial_objective_config in PolynomialObjective.CONFIG_SPACE
        ObjectiveFunctionBase.__init__(self, objective_function_config)

        # Let's start building the parameter space for it.
        #
        self._parameter_space = SimpleHypergrid(
            name="domain",
            dimensions=[
                CategoricalDimension(name="polynomial_id", values=[id for id in range(self.objective_function_config.num_nested_polynomials)])
            ]
        )

        polynomial_objective_config = self.objective_function_config.polynomial_objective_config
        self._polynomials = []
        # Let's create the required number of polynomials.
        #
        for i in range(self.objective_function_config.num_nested_polynomials):
            polynomial_objective_config.seed += i + 1 # Change the seed so that it's still effective but also reproducible.
            polynomial = PolynomialObjectiveWrapper(polynomial_objective_config, domain_name=f"domain_{i}")
            self._polynomials.append(polynomial)
            self._parameter_space.join(
                subgrid=polynomial.parameter_space,
                on_external_dimension=CategoricalDimension(name="polynomial_id", values=[i])
            )

        self._output_space = SimpleHypergrid(
            name='output_space',
            dimensions=[
                ContinuousDimension(name='y', min=-math.inf, max=math.inf)
            ]
        )

    @property
    def parameter_space(self) -> Hypergrid:
        return self._parameter_space

    @property
    def output_space(self) -> Hypergrid:
        return self._output_space

    def evaluate_point(self, point: Point) -> Point:
        selected_polynomial = self._polynomials[point.polynomial_id]
        return selected_polynomial.evaluate_point(point[f"domain_{point.polynomial_id}"])

    def evaluate_dataframe(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        # For now:
        values = []
        for i in range(len(dataframe.index)):
            row = dataframe.loc[[i]]
            point = Point.from_dataframe(row)
            value = self.evaluate_point(point)
            values.append(value.y)
        return pd.DataFrame({'y': values})


    def get_context(self) -> Point:
        """ Returns the config used to create the polynomial.

        Down the road it could return some more info about the resulting polynomial.

        :return:
        """
        return self._polynomial_objective_config
