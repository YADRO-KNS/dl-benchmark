from ..config_parser.test_reporter import Test


class TensorFlowLiteTest(Test):
    def __init__(self, model, dataset, indep_parameters, dep_parameters):
        super().__init__(model, dataset, indep_parameters, dep_parameters)

    def get_report(self):
        other_param = ', '.join([f'Device: {self.indep_parameters.device}',
                                 f'Iteration count: {self.indep_parameters.iteration}',
                                 f'Thread count: {self.dep_parameters.nthreads}',
                                 f'Channel swap: {self.dep_parameters.channel_swap}',
                                 f'Shape: {self.dep_parameters.input_shape}',
                                 f'Layout: {self.dep_parameters.layout}',
                                 f'Mean: {self.dep_parameters.mean}',
                                 f'Scale: {self.dep_parameters.input_scale}',
                                 f'Delegate: {self.dep_parameters.delegate}',
                                 f'Delegate options: {self.dep_parameters.delegate_options}'])

        report_res = {
            'task': self.model.task,
            'model': self.model.name,
            'dataset': self.dataset.name,
            'source_framework': self.model.source_framework,
            'inference_framework': self.indep_parameters.inference_framework,
            'precision': self.model.precision,
            'batch_size': self.indep_parameters.batch_size,
            'mode': 'Sync',
            'framework_params': other_param,
        }

        return report_res
